from fasthtml.common import *
from fasthtml.svg import *

from modules.shared.templates import page_template


@page_template(title="404")
def custom_404_handler(request, exc):
    return Section(
        Div(
            Div(
                H1(
                    "404",
                    cls="mb-4 text-7xl tracking-tight font-extrabold lg:text-9xl text-primary-600 dark:text-primary-500",
                ),
                P(
                    "Something's missing.",
                    cls="mb-4 text-3xl tracking-tight font-bold text-gray-900 md:text-4xl dark:text-white",
                ),
                P(
                    "Sorry, we can't find that page. You'll find lots to explore on the home page.",
                    cls="mb-4 text-lg font-light text-gray-500 dark:text-gray-400",
                ),
                A(
                    "Back to Homepage",
                    href="#",
                    cls="inline-flex text-white bg-primary-600 hover:bg-primary-800 focus:ring-4 focus:outline-none focus:ring-primary-300 font-medium rounded-lg text-sm px-5 py-2.5 text-center dark:focus:ring-primary-900 my-4",
                ),
                cls="mx-auto max-w-screen-sm text-center",
            ),
            cls="py-8 px-4 mx-auto max-w-screen-xl lg:py-16 lg:px-6",
        ),
        cls="bg-white dark:bg-gray-900",
    )
