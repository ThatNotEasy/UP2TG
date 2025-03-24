import os
import subprocess
import argparse
from modules.banners import banners
from modules.logging import setup_logging
from typing import List, Optional
from colorama import Fore, init

init(autoreset=True)

SUCCESS_COLOR = Fore.GREEN
ERROR_COLOR = Fore.RED
INFO_COLOR = Fore.CYAN
WARNING_COLOR = Fore.YELLOW

logger = setup_logging()

def upload_to_telegram(file_path: str, options: Optional[List[str]] = None) -> None:
    command = ['telegram-upload', file_path]
    if options:
        command.extend(options)
    try:
        logger.info(f"{INFO_COLOR}Attempting to upload file: {file_path}")
        subprocess.run(command, check=True)
        logger.info(f"{SUCCESS_COLOR}File uploaded successfully: {file_path}")
    except subprocess.CalledProcessError as e:
        logger.error(f"{ERROR_COLOR}Error uploading file {file_path}: {e}")
    except FileNotFoundError:
        logger.error(f"{ERROR_COLOR}Command 'telegram-upload' not found. Please install it.")

def build_telegram_upload_command(args: argparse.Namespace) -> List[str]:
    options = []
    if args.to:
        options.extend(['--to', args.to])
        logger.info(f"{INFO_COLOR}Setting destination to: {args.to}")
    if args.config:
        options.extend(['--config', args.config])
        logger.info(f"{INFO_COLOR}Using config file: {args.config}")
    if args.delete_on_success:
        options.append('-d')
        logger.info(f"{INFO_COLOR}Enabled delete on success.")
    if args.print_file_id:
        options.append('--print-file-id')
        logger.info(f"{INFO_COLOR}Enabled print file ID.")
    if args.force_file:
        options.append('--force-file')
        logger.info(f"{INFO_COLOR}Enabled force file.")
    if args.forward:
        options.extend(['-f', *args.forward])
        logger.info(f"{INFO_COLOR}Forwarding to: {args.forward}")
    if args.directories:
        options.extend(['--directories', args.directories])
        logger.info(f"{INFO_COLOR}Directory handling set to: {args.directories}")
    if args.large_files:
        options.extend(['--large_files', args.large_files])
        logger.info(f"{INFO_COLOR}Large file handling set to: {args.large_files}")
    if args.caption:
        options.extend(['--caption', args.caption])
        logger.info(f"{INFO_COLOR}Setting caption: {args.caption}")
    if args.no_thumbnail:
        options.append('--no-thumbnail')
        logger.info(f"{INFO_COLOR}Disabled thumbnail generation.")
    if args.thumbnail_file:
        options.extend(['--thumbnail-file', args.thumbnail_file])
        logger.info(f"{INFO_COLOR}Using thumbnail file: {args.thumbnail_file}")
    if args.proxy:
        options.extend(['-p', args.proxy])
        logger.info(f"{INFO_COLOR}Using proxy: {args.proxy}")
    if args.album:
        options.append('-a')
        logger.info(f"{INFO_COLOR}Enabled album mode.")
    if args.interactive:
        options.append('-i')
        logger.info(f"{INFO_COLOR}Enabled interactive mode.")
    if args.sort:
        options.append('--sort')
        logger.info(f"{INFO_COLOR}Enabled file sorting.")
    return options

def validate_file_paths(file_paths: List[str]) -> List[str]:
    valid_paths = []
    for file_path in file_paths:
        if os.path.exists(file_path):
            valid_paths.append(file_path)
            logger.info(f"{INFO_COLOR}File found: {file_path}")
        else:
            logger.error(f"{ERROR_COLOR}File not found: {file_path}")
    return valid_paths

def main() -> None:
    parser = argparse.ArgumentParser(description='Upload files to Telegram')
    parser.add_argument('file_path', nargs='+', help='Path(s) to the file(s) to upload')
    parser.add_argument('--to', help='Phone number, username, invite link or "me" (saved messages). By default "me".')
    parser.add_argument('--config', help='Configuration file to use. By default "/root/.config/telegram-upload.json".')
    parser.add_argument('-d', '--delete-on-success', action='store_true', help='Delete local file after successful upload.')
    parser.add_argument('--print-file-id', action='store_true', help='Print the id of the uploaded file after the upload.')
    parser.add_argument('--force-file', action='store_true', help='Force send as a file. The filename will be preserved but the preview will not be available.')
    parser.add_argument('-f', '--forward', nargs='+', help='Forward the file to a chat (alias or id) or user (username, mobile or id). This option can be used multiple times.')
    parser.add_argument('--directories', choices=['fail', 'recursive'], help='Defines how to process directories. By default directories are not accepted and will raise an error.')
    parser.add_argument('--large-files', choices=['fail', 'split'], help='Defines how to process large files unsupported for Telegram. By default large files are not accepted and will raise an error.')
    parser.add_argument('--caption', help='Change file description. By default the file name.')
    parser.add_argument('--no-thumbnail', action='store_true', help='Disable thumbnail generation. For some known file formats, Telegram may still generate a thumbnail or show a preview.')
    parser.add_argument('--thumbnail-file', help='Path to the preview file to use for the uploaded file.')
    parser.add_argument('-p', '--proxy', help='Use an http proxy, socks4, socks5 or mtproxy.')
    parser.add_argument('-a', '--album', action='store_true', help='Send video or photos as an album.')
    parser.add_argument('-i', '--interactive', action='store_true', help='Use interactive mode.')
    parser.add_argument('--sort', action='store_true', help='Sort files by name before upload it.')

    args = parser.parse_args()
    logger.info(f"{INFO_COLOR}Validating file paths...")
    valid_file_paths = validate_file_paths(args.file_path)
    if not valid_file_paths:
        logger.error(f"{ERROR_COLOR}No valid files to upload.")
        return

    options = build_telegram_upload_command(args)
    logger.info(f"{INFO_COLOR}Starting file uploads...")
    for file_path in valid_file_paths:
        upload_to_telegram(file_path, options)

    logger.info(f"{SUCCESS_COLOR}Script execution completed.")

if __name__ == "__main__":
    banners()
    main()