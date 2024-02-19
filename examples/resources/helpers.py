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
    return os.path.normpath(os.path.join(host, urllib.request.url2pathname(parsed.path)))


def bootstrap(manager_config_toml_path: str):
    """
    Encapsulate the common bootstrapping code used in multiple
    notebooks.
    """
    try:
        from pprint import pprint
        from resources import helpers
        import openassetio
        import openassetio_mediacreation
    except ImportError:
        print(
            "This notebook requires the packages listed in"
            " `resources/requirements.txt` to be installed"
        )
        raise

    from openassetio.hostApi import HostInterface, ManagerFactory
    from openassetio.log import ConsoleLogger, SeverityFilter
    from openassetio.pluginSystem import PythonPluginSystemManagerImplementationFactory

    class NotebookHostInterface(HostInterface):
        def identifier(self):
            return "org.jupyter.notebook"

        def displayName(self):
            return "Jupyter Notebook"

    host_interface = NotebookHostInterface()

    logger = SeverityFilter(ConsoleLogger())

    impl_factory = PythonPluginSystemManagerImplementationFactory(logger)

    manager = ManagerFactory.defaultManagerForInterface(
        manager_config_toml_path,
        host_interface,
        impl_factory,
        logger,
    )

    context = manager.createContext()

    return manager, context
