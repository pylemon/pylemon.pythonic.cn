# -*- coding: utf-8 -*-
#: settings for liquidluck

#: site information
#: all variables can be accessed in template with ``site`` namespace.
#: for instance: {{site.name}}
site = {
    "name": "pyLemon's Notebook",  # your site name
    "url": "http://pylemon.pythonic.cn/",  # your site url
    # "prefix": "blog",
}

#: this config defined information of your site
#: 1. where the resources  2. how should the site be generated
config = {
    "source": "content",
    "output": "_site",
    "static": "_site/static",
    # "static_prefix": "/static/",
    "permalink": "{{date.year}}/{{filename}}.html",
    "relative_url": False,
    "perpage": 30,
    # "feedcount": 20,
    "timezone": "+08:00",
}


author = {
    "default": "pyLemon",
    "vars": {
        'pyLemon': {
            'name': 'Lemon Li',
            'website': 'http://pylemon.pythonic.cn/',
            'email': 'leeway1985@gmail.com',
        }
    }
}

#: active readers
reader = {
    "active": [
        "liquidluck.readers.markdown.MarkdownReader",
        # uncomment to active rst reader.
        # but you need to install docutils by yourself
        # "liquidluck.readers.restructuredtext.RestructuredTextReader",
    ],
    "vars": {}
}

#: active writers
writer = {
    "active": [
        "liquidluck.writers.core.PostWriter",
        "liquidluck.writers.core.PageWriter",
        "liquidluck.writers.core.ArchiveWriter",
        "liquidluck.writers.core.ArchiveFeedWriter",
        "liquidluck.writers.core.FileWriter",
        "liquidluck.writers.core.StaticWriter",
        "liquidluck.writers.core.YearWriter",
        "liquidluck.writers.core.CategoryWriter",
        "liquidluck.writers.core.CategoryFeedWriter",
        "liquidluck.writers.core.TagWriter",
        "liquidluck.writers.core.TagCloudWriter",
    ],
    "vars": {
        # uncomment if you want to reset archive page
        "archive_output": "archive.html",
    }
}

#: theme variables
theme = {
    "name": "moment",

    # theme variables are defined by theme creator
    # you can access theme in template with ``theme`` namespace
    # for instance: {{theme.disqus}}
    "vars": {
        "disqus": "pylemonsblog",
        "analytics": "UA-37174347-1",
        'allow_comment_on_secret_post': True,
        
        'navigation': [
            {'name': 'Blog', 'link': '/archive/'},
            {'name': 'Life', 'link': '/life/'},
            {'name': 'Work', 'link': '/work/'},
            {'name': 'Resume', 'link': '/resume/'},
        ],
        
        'elsewhere': [
            {'name': 'GitHub', 'link': 'https://github.com/pylemon'},
            {'name': 'Twitter', 'link': 'https://twitter.com/leeway1985'},
        ],
        
        'descriptions': {
            'life': 'I love python!',
            'work': 'works with Python, Emacs, Javascript, Linux, MacOS, etc..'
        },

    }
}

#: template variables
template = {
    "vars": {},
    "filters": {},
}
