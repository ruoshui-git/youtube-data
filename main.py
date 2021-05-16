from datetime import datetime
from typing import Optional
from youtube_data.models import VideoInfo
from youtube_data.scraper import Scraper
import typer
from pathlib import Path


def main(link: str = typer.Argument('https://www.youtube.com/playlist?list=UUkss6NzmCBzo8TyvB3I0qaA', help="YouTube playlist link as entry point"),
         max_videos: Optional[int] = typer.Option(
             None, help='Max number of videos to get'),
         comments: bool = typer.Option(
             False, help="Get actual comments, but will run a lot slower"),
         summary: bool = typer.Option(
             True, help="Show total values in the end"),
         progress: bool = typer.Option(
             False, help="Show progress bar; todo"),
         json: Optional[Path] = typer.Option(
             None, help="Output JSON file"),
         headless: bool = typer.Option(
             True, help="Run Chromedriver in headless mode")
         ):

    typer.secho(
        f"{datetime.now()}: starting Chrome webdriver in {('headless' if headless else 'GUI')} mode...", fg=typer.colors.YELLOW)
    scraper = Scraper(headless=headless)

    typer.echo(f"Entry point: {typer.style(link, fg=typer.colors.YELLOW)}")
    channel_info = scraper.scrape_playlist(
        link, max_videos=max_videos, get_comments=comments, print_info=False, show_progress=progress)

    typer.secho(
        f'Done scraping videos.', fg=typer.colors.GREEN)

    if json is not None:
        json.write_text(channel_info.to_json(  # type:ignore
            ensure_ascii=False), encoding="utf-8")
        typer.secho(
            f'JSON written to {json.absolute()}', fg=typer.colors.GREEN)

    # if summary:
    if summary:
        typer.echo('='*20)
        typer.echo('Total:')
        typer.echo(f'views: {channel_info.total_views}')
        typer.echo(f'comments: {channel_info.total_comments}')
        typer.echo(f'likes: {channel_info.total_likes}')
        typer.echo(f'dislikes: {channel_info.total_dislikes}')

    typer.echo(f'{datetime.now()}: Done.')


if __name__ == "__main__":
    typer.run(main)
