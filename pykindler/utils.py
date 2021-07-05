from os import path
import logging

logger = logging.getLogger(__name__)


def trigger_conversion(absolute_file_path, processed_dir, convert_dir, extension):
    from subprocess import check_output
    from os import rename

    filename = path.basename(absolute_file_path)
    logger.info(f"Beginning conversion: {filename}")
    check_output(
        [
            "ebook-convert",
            absolute_file_path,
            path.join(
                convert_dir,
                filename[: filename.rfind(".")] + "." + extension,
            ),
        ]
    )
    rename(absolute_file_path, path.join(processed_dir, filename))
    logger.info(f"Completed Conversion: {filename}")
