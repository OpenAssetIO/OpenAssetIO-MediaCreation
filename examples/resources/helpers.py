import os

from IPython.display import display, display_markdown
from PIL import Image
import urllib


def display_result(result):
    """
    Displays the suppied result in a block quote with a 'result'
    heading. Tuples/lists are rendered as one item per line in a
    markdown list.
    """
    output = "> **Result:**\n"
    if isinstance(result, (list, tuple)):
        output += "\n".join([f"> - `{r}`" for r in result])
    else:
        output += f"> `{result}`"
    display_markdown(output, raw=True)


def display_image(url):
    """
    Displays an image in the notebook output.
    """
    image = Image.open(path_from_url(url))
    display(image)


def path_from_url(url):
    """
    Attempts to extract a path from a file URL in a cross-platform way.
    """
    # Adapted from https://stackoverflow.com/a/61922504/535103
    parsed = urllib.parse.urlparse(url)
    host = "{0}{0}{mnt}{0}".format(os.path.sep, mnt=parsed.netloc)
    return os.path.normpath(
        os.path.join(host, urllib.request.url2pathname(parsed.path))
    )
