try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup, find_packages


setup(
    name="scrapoxy",
    packages=find_packages(),
    install_requires=["requests"],
    version="1.12",
    description="Use Scrapoxy with Scrapy",
    author="OctopusMind Team",
    author_email="it@octopusmind.info",
    url="https://github.com/jurismarches/scrapoxy-py",
    download_url="https://github.com/jurismarches/scrapoxy-py/archive/refs/heads/main.zip",
    keywords=["crawler", "crawling", "scrapoxy", "scrapy", "scraper", "scraping"],
    classifiers=[],
)
