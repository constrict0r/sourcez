# Configuration file for the Sphinx documentation builder.

import os
import sys

project = "sourcez"
copyright = "2019, constrict0r"
author = "constrict0r"
version = "0.0.1"
release = "0.0.1"

sys.path.insert(0, os.path.abspath("../.."))

extensions = [
    "sphinxcontrib.restbuilder",
    "sphinxcontrib.globalsubs",
    "sphinx-prompt",
    "sphinx_substitution_extensions"
]

templates_path = ["_templates"]

exclude_patterns = []

html_static_path = ["_static"]

html_theme = "sphinx_rtd_theme"

master_doc = "index"

img_base_url = "https://gitlab.com/" + author + "/img/raw/master/"
img_url = img_base_url + project + "/"

author_img = ".. image:: " + img_url + "author.png\n   :alt: author"
author_slogan = "The Travelling Vaudeville Villain."

github_base_url = "https://github.com/"
github_url = github_base_url + author + "/" + project
github_link = "`Github <" + github_url + ">`_."

gitlab_base_url = "https://gitlab.com/"
gitlab_url = gitlab_base_url + author + "/" + project
gitlab_badge = gitlab_url + "/badges/master/pipeline.svg\n   :alt: pipeline"
gitlab_ci_url = gitlab_url + "/pipelines"
gitlab_ci_link = "`Gitlab CI <" + gitlab_ci_url + ">`_."
gitlab_link = "`Gitlab <" + gitlab_url + ">`_."

travis_base_url = "https://travis-ci.com/"
travis_url = travis_base_url + author + "/" + project
travis_badge = ".. image:: " + travis_url + ".svg\n   :alt: travis"
travis_ci_url = travis_url
travis_link = "`Travis CI <" + travis_url + ">`_."

readthedocs_url = "https://" + project + ".readthedocs.io"
readthedocs_badge = "/projects/" + project + "/badge\n   :alt: readthedocs"
readthedocs_link = "`Readthedocs <" + readthedocs_url + ">`_."

global_substitutions = {
    "AUTHOR_IMG": author_img,
    "AUTHOR_SLOGAN": author_slogan,
    "AVATAR_IMG": ".. image:: " + img_url + "avatar.png\n   :alt: avatar",
    "DEFAULT_VAR_NAME": 'repositories',
    "DEPLOY_IMG": ".. image:: " + img_url + "/deploy.png\n   :alt: deploy",
    "DOOMBOT_IMG": ".. image:: " + img_url + "/doombot.png\n   :alt: doombot",
    "ENJOY_IMG": ".. image:: " + img_url + "/enjoy.png\n   :alt: enjoy",
    "GITLAB_BADGE":  ".. image:: " + gitlab_badge,
    "GITLAB_CI_LINK":  gitlab_ci_link,
    "GITHUB_LINK":  github_link,
    "GITLAB_LINK":  gitlab_link,
    "INGREDIENT_IMG": ".. image:: " + img_url +
    "/ingredient.png\n   :alt: ingredient",
    "MAIN_IMG": ".. image:: " + img_url + "/main.png\n   :alt: main",
    "PROJECT": project,
    "READTHEDOCS_BADGE": ".. image:: https://rtfd.io" + readthedocs_badge,
    "READTHEDOCS_LINK": readthedocs_link,
    "TRAVIS_BADGE": travis_badge,
    "TRAVIS_LINK": travis_link
}

repo_name = '[{name: multimedia, repo: '
repo_url = '\'deb http://www.debian-multimedia.org sid main\'}]'
repo_var = '-e "{repositories: ' + repo_name + repo_url + '}"'

substitutions = [
    ("|AUTHOR|", author),
    ("|DEFAULT_ROLE_VARS|", repo_var),
    ("|DEFAULT_VAR_NAME|", 'repositories'),
    ("|DEFAULT_VAR_VALUE|", repo_name + repo_url),
    ("|PROJECT|", project)
]
