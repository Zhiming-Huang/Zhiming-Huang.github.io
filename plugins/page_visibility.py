"""
Page visibility controls for Pelican.

Markdown pages can set:
  Publish: false  -> do not write the page to output
  Menu: true      -> show the page in the navbar template
"""

from pelican import signals


FALSE_VALUES = {"false", "no", "0", "off"}


def _is_false(value):
    return str(value).strip().lower() in FALSE_VALUES


def _should_publish(page):
    return not _is_false(getattr(page, "publish", "true"))


def filter_unpublished_pages(generator):
    """Remove pages marked Publish: false before Pelican writes output files."""
    page_groups = (
        "pages",
        "translations",
        "hidden_pages",
        "hidden_translations",
        "draft_pages",
        "draft_translations",
    )

    removed = 0
    for group in page_groups:
        pages = getattr(generator, group, [])
        kept = [page for page in pages if _should_publish(page)]
        removed += len(pages) - len(kept)
        setattr(generator, group, kept)
        generator.context[group] = kept

    if removed:
        print(f"Skipped {removed} unpublished page(s)")


def register():
    signals.page_generator_finalized.connect(filter_unpublished_pages)
