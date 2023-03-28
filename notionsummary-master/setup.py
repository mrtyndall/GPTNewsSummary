from setuptools import setup, find_packages

setup(
    name='news_summary_app',
    version='1.0',
    author='Priceless Misc',
    author_email='matt@pricelessmisc.com',
    description='A Python app that generates summaries for news articles',
    packages=find_packages(),
    install_requires=[
        'newspaper3k==0.2.8',
        'openai==0.10.3',
        'Flask==2.0.1',
        'notion-client==0.6.1'
    ],
    entry_points={
        'console_scripts': [
            'news-summary-app=news_summary_app:main'
        ]
    }
)
