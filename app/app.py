"""Reflex application entry point."""

import reflex as rx


def index() -> rx.Component:
    return rx.el.main(
        rx.el.div(
            rx.icon("shield-check", class_name="h-8 w-8 text-blue-600"),
            rx.el.h1(
                "RVG Gateway", class_name="text-2xl font-semibold text-gray-900"
            ),
            rx.el.p(
                "The application is available.",
                class_name="text-base font-medium text-gray-600",
            ),
            class_name="flex flex-col items-center gap-4 rounded-xl border border-gray-200 bg-white p-8 text-center",
        ),
        class_name="flex min-h-screen items-center justify-center bg-gray-50 p-6",
    )


app = rx.App(theme=rx.theme(appearance="light"))
app.add_page(index, route="/")
