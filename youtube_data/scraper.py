from datetime import datetime
from time import sleep
from typing import List, Optional, Set, Tuple

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver import ChromeOptions
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import typer

from .models import ChannelInfo, CommentInfo, VideoInfo


class Scraper:
    driver: WebDriver

    def __init__(self, headless: bool = False, chrome_src: str = r'C:\Program Files\Google\Chrome Beta\Application\chrome.exe') -> None:
        ops = ChromeOptions()
        ops.binary_location = chrome_src
        ops.headless = headless
        # Suppress some Selenium logs. Use `--log-level=OFF` for complete silence
        ops.add_argument('--log-level=3')
        driver = webdriver.Chrome(options=ops)

        driver.set_window_position(0, 0)
        driver.set_window_size(723, 657)

        self.driver = driver

    def __del__(self):
        try:
            self.driver.quit()
        except AttributeError:
            pass

    def zoom_in(self, level: int):
        """
        Zoom in `level` many times
        """
        html: WebElement = self.driver.find_element_by_tag_name('html')

        for _ in range(level):
            ActionChains(self.driver).key_down(Keys.CONTROL).send_keys(
                '-').key_up(Keys.CONTROL).perform()

    def scroll(self, height: int):
        """
        Scroll window down vertically
        """
        self.driver.execute_script(f'window.scrollBy(0,{height})')

    def scroll_to_comments(self):
        """
        Scroll comments into view so related data is loaded
        """
        comments: WebElement = self.driver.find_element_by_tag_name(
            'ytd-comments')
        self.driver.execute_script(
            "arguments[0].scrollIntoView(true)", comments)
        # comments.location_once_scrolled_into_view

    def load_all_comments(self):
        """
        Load all comments by scrolling and waiting for `yt-next-continuation` to disapplear

        Raise Exception if page is just initialized and comments are not loaded by scrolling down
        """
        try:
            self.driver.find_element_by_css_selector(
                'ytd-comments #continuations')
        except NoSuchElementException:
            raise Exception(
                "Comments not loaded yet before trying to load them all")

        while True:
            try:
                self.driver.find_element_by_css_selector(
                    'div#continuations yt-next-continuation')
                self.scroll(10000)
                sleep(1)
            except NoSuchElementException:
                return

    def scrolled_to_bottom(self) -> bool:
        """
        Checks if page is scrolled to the bottom
        """
        return self.driver.execute_script("(window.innerHeight + window.scrollY) >= document.querySelectorAll('.ytd-app#content')[0].scrollHeight")

    def get_comment_info(self, comment: WebElement):
        """
        Returns extracted info of a comment
        """
        author: str = comment.find_element_by_css_selector(
            '#header-author a').text
        text: str = comment.find_element_by_id('content-text').text

        return CommentInfo(author, text)

    def get_video_info(self, info: Tuple[str, str], get_comments: bool) -> VideoInfo:
        """
        Get video information for a single video
        """

        vd_name, vd_link = info

        self.driver.get(vd_link)

        vc_text: WebElement = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, 'view-count'))
        )

        view_count = int(vc_text.text.replace(',','').split(' ')[0])

        likes_elems: List[WebElement] = self.driver.find_elements_by_css_selector(
            'yt-formatted-string#text.style-scope.ytd-toggle-button-renderer.style-text')

        likes = int(likes_elems[0].text)
        dislikes = int(likes_elems[1].text)

        # Load comment count and comments; This value is window size specific
        # self.scroll(2000)

        self.scroll_to_comments()

        # for _ in range(30):
        #     try:
        #         # self.driver.find_element_by_css_selector(
        #         # 'yt-formatted-string.count-text')
        #         comment_str: str = WebDriverWait(self.driver, 0.3).until(
        #             EC.presence_of_element_located(
        #                 (By.CSS_SELECTOR, 'yt-formatted-string.count-text'))
        #         ).text
        #     # except NoSuchElementException:
        #     except TimeoutException:
        #         self.scroll(100)

        comment_str = '-1 Comments'
        for _ in range(20):
            try:
                comment_str: str = WebDriverWait(self.driver, 0.5).until(
                    EC.presence_of_element_located(
                        (By.CSS_SELECTOR, 'yt-formatted-string.count-text'))
                ).text
                break
            except TimeoutException:
                self.scroll_to_comments()

        comment_count = int(comment_str.split(' ')[0])
        comments: List[CommentInfo] = []
        # comments are almost guaranteed now

        # now we want to get the comment text
        if get_comments:
            if not comment_count == 0:
                comment_section: WebElement = self.driver.find_element_by_css_selector(
                    'div#contents.style-scope.ytd-item-section-renderer')

                comments_elem: List[WebElement] = []
                self.load_all_comments()

                num_comments_no_expand = len(comment_section.find_elements_by_tag_name(
                    'ytd-comment-renderer'))
                self.expand_replies(comment_section, num_comments_no_expand)
                comments_elem: List[WebElement] = comment_section.find_elements_by_tag_name(
                    'ytd-comment-renderer')

                for comment_elem in comments_elem:
                    comments.append(self.get_comment_info(comment_elem))

        # return
        return VideoInfo(vd_name, vd_link, view_count, likes, dislikes, comment_count, comments)

    def expand_replies(self, comments: WebElement, num_comments_before):
        """
        Select for the 'View [number] Replies' button and click on them

        `num_comments_before` is used to check expansion
        """

        # use this to select "view reply" button
        # ytd-button-renderer.ytd-comment-replies-renderer#more-replies

        # btns: List[WebElement] = comments.find_elements_by_css_selector(
        #     'ytd-button-renderer.ytd-comment-replies-renderer#more-replies')
        # for btn in btns:
        #     btn.click()

        # Avoid click errors
        reply_button_selector = 'ytd-button-renderer.ytd-comment-replies-renderer#more-replies'
        if self.driver.execute_script(f'''return document.querySelectorAll('{reply_button_selector}').length === 0'''):
            return

        self.driver.execute_script(
            f'''document.querySelectorAll('{reply_button_selector}').forEach(e => e.click());''')

        while True:
            num = len(self.driver.find_elements_by_tag_name(
                'ytd-comment-renderer'))
            if (num == num_comments_before):
                sleep(0.3)
            else:
                return

    def scrape_playlist(self, playlist_link: str, max_videos: Optional[int], get_comments: bool, print_info: bool, show_progress: bool) -> ChannelInfo:
        """
        Get all information
        """
        typer.echo('Getting playlist information...')

        self.driver.get(playlist_link)

        video_list: List[Tuple[str, str]] = []

        elems: List[WebElement] = WebDriverWait(self.driver, 10).until(
            EC.presence_of_all_elements_located(
                (By.CSS_SELECTOR,
                    'ytd-playlist-video-renderer[lockup]'))
        )

        for item in elems:
            link: str = item.find_element_by_tag_name(
                'a').get_attribute('href')
            name: str = item.find_element_by_id('video-title').text

            video_list.append((name, link))

        # sort videos by name
        video_list.sort(key=lambda x: x[0])

        stats: List[VideoInfo] = []

        typer.echo(
            f'Found {len(video_list)} videos.')

        if max_videos:
            typer.secho(
                f'Only processing {max_videos} video links.', fg=typer.colors.YELLOW)
            video_list = video_list[:max_videos]

        with typer.progressbar(video_list, label="Scraping single videos") as vs:

            for video in vs:
                stat = self.get_video_info(video, get_comments=get_comments)
                if print_info:
                    typer.echo('='*20)
                    typer.echo(stat)
                stats.append(stat)

        typer.echo("Computing stats...")

        total_views = 0
        total_likes = 0
        total_dislikes = 0
        total_comments = 0
        total_commenters = None

        # typer.echo('='*20)
        for video in stats:
            total_views += video.view_count
            total_likes += video.likes
            total_dislikes += video.dislikes
            total_comments += video.comment_count

        if get_comments:
            commenters: Set[str] = set()
            for video in stats:
                commenters.update(
                    comment.author for comment in video.comments)
            total_commenters = len(commenters)
        else:
            total_commenters = None

        return ChannelInfo(stats, datetime.now(), total_likes, total_dislikes, total_views, total_comments, total_commenters)
