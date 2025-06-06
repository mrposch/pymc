"""Sphinx configuration file."""
#!/usr/bin/env python3
#
# pymc documentation build configuration file, created by
# sphinx-quickstart on Sat Dec 26 14:40:23 2015.
#
# This file is execfile()d with the current directory set to its
# containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

import os

from pathlib import Path

import pymc

# -- General configuration ------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
# needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    "matplotlib.sphinxext.plot_directive",
    "sphinx.ext.autodoc",
    "sphinx.ext.autosummary",
    "sphinx.ext.viewcode",
    "sphinx.ext.mathjax",
    "sphinx.ext.intersphinx",
    "numpydoc",
    "IPython.sphinxext.ipython_console_highlighting",
    "IPython.sphinxext.ipython_directive",
    "myst_nb",
    "sphinx_design",
    "notfound.extension",
    "sphinx_copybutton",
    "sphinx_remove_toctrees",
    "jupyter_sphinx",
    "sphinxext.rediraffe",
    "sphinx_sitemap",
]

# Don't auto-generate summary for class members.
numpydoc_show_class_members = False
autosummary_generate = True
autodoc_typehints = "none"
remove_from_toctrees = ["**/classmethods/*"]

numpydoc_xref_param_type = True
# fmt: off
numpydoc_xref_ignore = {
    "of", "or", "optional", "default", "numeric", "type", "scalar", "1D", "2D", "3D", "nD", "array",
    "instance", "M", "N"
}
# fmt: on
numpydoc_xref_aliases = {
    "TensorVariable": ":class:`~pytensor.tensor.TensorVariable`",
    "RandomVariable": ":class:`~pytensor.tensor.random.RandomVariable`",
    "ndarray": ":class:`~numpy.ndarray`",
    "Covariance": ":mod:`Covariance <pymc.gp.cov>`",
    "Mean": ":mod:`Mean <pymc.gp.mean>`",
    "InferenceData": ":class:`~arviz.InferenceData`",
    "MultiTrace": ":class:`~pymc.backends.base.MultiTrace`",
    "BaseTrace": ":class:`~pymc.backends.base.BaseTrace`",
    "Point": ":class:`~pymc.Point`",
    "Model": ":class:`~pymc.Model`",
    "SMC_kernel": ":ref:`SMC Kernel <smc_kernels>`",
    "PyTensor_Op": ":class:`PyTensor Op <pytensor.graph.op.Op>`",
    "tensor_like": ":term:`tensor_like`",
    "unnamed_distribution": ":term:`unnamed_distribution`",
    "numpy_Generator": ":class:`~numpy.random.Generator`",
    "Distribution": ":ref:`Distribution <api_distributions>`",
}

# Show the documentation of __init__ and the class docstring
# autoclass_content = "both"

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
# source_suffix = ['.rst', '.md']
source_suffix = [".rst", ".md"]

# The encoding of source files.
# source_encoding = 'utf-8-sig'

# The master toctree document.
master_doc = "index"

# General information about the project.
project = "PyMC"
copyright = "2020-present, The PyMC Development Team"
author = "PyMC contributors"

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.

version = pymc.__version__
on_readthedocs = os.environ.get("READTHEDOCS", False)
rtd_version = os.environ.get("READTHEDOCS_VERSION", "")
if on_readthedocs:
    if rtd_version.lower() == "stable":
        version = pymc.__version__.split("+")[0]
    elif rtd_version.lower() == "latest":
        version = "dev"
    else:
        version = rtd_version
else:
    rtd_version = "local"
# The full version, including alpha/beta/rc tags.
release = version

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = "en"

# configure notfound extension to not add any prefix to the urls
notfound_urls_prefix = "/projects/docs/en/latest/"

# There are two options for replacing |today|: either, you set today to some
# non-false value, then it is used:
# today = ''
# Else, today_fmt is used as the format for a strftime call.
# today_fmt = '%B %d, %Y'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
exclude_patterns = [
    "_build",
    "**.ipynb_checkpoints",
    "pymc-examples/.github",
    "about/featured_testimonials.md",
]

# myst config
# Use commented code after https://github.com/pymc-devs/pymc/issues/7384 is fixed
# nb_execution_mode = "force" if on_readthedocs else "off"
nb_execution_mode = "off"
nb_execution_allow_errors = False
nb_execution_raise_on_error = True
nb_execution_timeout = 300
nb_kernel_rgx_aliases = {".*": "python3"}
myst_enable_extensions = ["colon_fence", "deflist", "dollarmath", "amsmath", "substitution"]
myst_substitutions = {
    "version_slug": rtd_version,
}
myst_heading_anchors = 0

v3_example_tutorials = [
    "case_studies/BEST",
    "case_studies/LKJ",
    "case_studies/stochastic_volatility",
    "case_studies/rugby_analytics",
    "case_studies/multilevel_modeling",
    "case_studies/putting_workflow",
    "case_studies/moderation_analysis",
    "case_studies/mediation_analysis",
    "case_studies/bayesian_ab_testing",
    "case_studies/item_response_nba",
    "diagnostics_and_criticism/Diagnosing_biased_Inference_with_Divergences",
    "diagnostics_and_criticism/Bayes_factor",
    "generalized_linear_models/GLM-logistic",
    "generalized_linear_models/GLM-binomial-regression",
    "generalized_linear_models/GLM-hierarchical-binominal-model",
    "generalized_linear_models/GLM-hierarchical",
    "case_studies/hierarchical_partial_pooling",
    "generalized_linear_models/GLM-model-selection",
    "generalized_linear_models/GLM-negative-binomial-regression",
    "generalized_linear_models/GLM-out-of-sample-predictions",
    "generalized_linear_models/GLM-poisson-regression",
    "generalized_linear_models/GLM-robust-with-outlier-detection",
    "generalized_linear_models/GLM-robust",
    "generalized_linear_models/GLM-rolling-regression",
    "generalized_linear_models/GLM-truncated-censored-regression",
    "generalized_linear_models/GLM-simpsons-paradox",
    "gaussian_processes/GP-Kron",
    "gaussian_processes/GP-Latent",
    "gaussian_processes/GP-Marginal",
    "gaussian_processes/GP-MaunaLoa",
    "gaussian_processes/GP-MaunaLoa2",
    "gaussian_processes/GP-MeansAndCovs",
    "gaussian_processes/GP-SparseApprox",
    "gaussian_processes/GP-TProcess",
    "gaussian_processes/GP-smoothing",
    "gaussian_processes/GP-Heteroskedastic",
    "gaussian_processes/gaussian_process",
    "case_studies/conditional-autoregressive-model",
    "case_studies/log-gaussian-cox-process",
    "gaussian_processes/GP-Circular",
    "mixture_models/dependent_density_regression",
    "mixture_models/dp_mix",
    "variational_inference/gaussian-mixture-model-advi",
    "mixture_models/gaussian_mixture_model",
    "mixture_models/marginalized_gaussian_mixture_model",
    "mixture_models/dirichlet_mixture_of_multinomials",
    "samplers/SMC2_gaussians",
    "samplers/SMC-ABC_Lotka-Volterra_example",
    "survival_analysis/bayes_param_survival_pymc3",
    "survival_analysis/censored_data",
    "survival_analysis/survival_analysis",
    "survival_analysis/weibull_aft",
    "survival_analysis/cox_model",
    "time_series/MvGaussianRandomWalk_demo",
    "time_series/AR",
    "time_series/Euler-Maruyama_and_SDEs",
    "time_series/Air_passengers-Prophet_with_Bayesian_workflow",
    "variational_inference/bayesian_neural_network_advi",
    "variational_inference/convolutional_vae_keras_advi",
    "variational_inference/empirical-approx-overview",
    "variational_inference/lda-advi-aevb",
    "variational_inference/normalizing_flows_overview",
    "variational_inference/gaussian-mixture-model-advi",
    "variational_inference/GLM-hierarchical-advi-minibatch",
    "ode_models/ODE_with_manual_gradients",
    "ode_models/ODE_API_introduction",
    "case_studies/probabilistic_matrix_factorization",
    "pymc3_howto/sampling_conjugate_step",
    "samplers/MLDA_introduction",
    "samplers/MLDA_simple_linear_regression",
    "samplers/MLDA_gravity_surveying",
    "samplers/MLDA_variance_reduction_linear_regression",
    "samplers/GLM-hierarchical-jax",
    "pymc3_howto/api_quickstart",
    "variational_inference/variational_api_quickstart",
    "Probability_Distributions.rst",
    "pymc3_howto/data_container",
    "pymc3_howto/sampling_compound_step",
    "pymc3_howto/sampling_callback",
    "diagnostics_and_criticism/sampler-stats",
    "diagnostics_and_criticism/Diagnosing_biased_Inference_with_Divergences",
    "Advanced_usage_of_Theano_in_PyMC3.rst",
    "ode_models/ODE_API_shapes_and_benchmarking",
    "samplers/DEMetropolisZ_EfficiencyComparison",
    "samplers/DEMetropolisZ_tune_drop_fraction",
    "case_studies/factor_analysis",
    "case_studies/blackbox_external_likelihood",
    "pymc3_howto/profiling",
    "pymc3_howto/howto_debugging",
    "diagnostics_and_criticism/model_averaging",
    "pymc3_howto/updating_priors",
    "pymc3_howto/lasso_block_update",
    "nb_examples/index.html",
    "nb_tutorials/index.html",
]
rediraffe_redirects = {
    "index.md": "learn.md",
    "pymc-examples/examples/getting_started.md": "learn/core_notebooks/pymc_overview.ipynb",
    "pymc-examples/examples/PyMC3_and_Theano.rst": "learn/core_notebooks/pymc_pytensor.ipynb",
    "pymc-examples/examples/generalized_linear_models/GLM.ipynb": "learn/core_notebooks/GLM_linear.ipynb",
    "pymc-examples/examples/generalized_linear_models/GLM-linear.ipynb": "learn/core_notebooks/GLM_linear.ipynb",
    "pymc-examples/examples/diagnostics_and_criticism/model_comparison.ipynb": "learn/core_notebooks/model_comparison.ipynb",
    "pymc-examples/examples/diagnostics_and_criticism/posterior_predictive.ipynb": "learn/core_notebooks/posterior_predictive.ipynb",
    "pymc-examples/examples/Gaussian_Processes.rst": "learn/core_notebooks/Gaussian_Processes.rst",
    **{
        f"pymc-examples/examples/{v3_path}.ipynb": "learn/core_notebooks/index.md"
        for v3_path in v3_example_tutorials
    },
}
# The reST default role (used for this markup: `text`) to use for all
# documents.
# default_role = None

# If true, '()' will be appended to :func: etc. cross-reference text.
# add_function_parentheses = True

# If true, the current module name will be prepended to all description
# unit titles (such as .. function::).
# add_module_names = True

# If true, sectionauthor and moduleauthor directives will be shown in the
# output. They are ignored by default.
# show_authors = False

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = "friendly"

# A list of ignored prefixes for module index sorting.
# modindex_common_prefix = []

# If true, keep warnings as "system message" paragraphs in the built documents.
# keep_warnings = False

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = False

# intersphinx configuration to ease linking arviz docs
intersphinx_mapping = {
    "arviz": ("https://python.arviz.org/en/latest/", None),
    "pytensor": ("https://pytensor.readthedocs.io/en/latest/", None),
    "home": ("https://www.pymc.io", None),
    "pmx": ("https://www.pymc.io/projects/experimental/en/latest", None),
    "numpy": ("https://numpy.org/doc/stable/", None),
    "nb": ("https://www.pymc.io/projects/examples/en/latest/", None),
    "myst": ("https://myst-parser.readthedocs.io/en/latest", None),
    "myst-nb": ("https://myst-nb.readthedocs.io/en/latest/", None),
    "python": ("https://docs.python.org/3/", None),
    "scipy": ("https://docs.scipy.org/doc/scipy/", None),
    "xarray": ("https://docs.xarray.dev/en/stable/", None),
    "zarr": ("https://zarr.readthedocs.io/en/stable/", None),
}


def remove_index(app):
    """
    This removes the index pages so rediraffe generates the redirect placeholder
    It needs to be present initially for the toctree as it defines the navbar.
    """

    index_file = Path(app.outdir) / "index.html"
    index_file.unlink()

    app.env.project.docnames -= {"index"}
    yield "", {}, "layout.html"


def setup(app):
    """
    Add extra step to sphinx build
    """

    app.connect("html-collect-pages", remove_index, 100)


# -- Options for HTML output ----------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
html_theme = "pymc_sphinx_theme"
html_baseurl = "https://www.pymc.io/projects/docs/"
sitemap_url_scheme = f"{{lang}}{rtd_version}/{{link}}"


# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.

html_theme_options = {
    "logo": {
        "link": "https://www.pymc.io",
    },
    "search_bar_text": "Search within PyMC library docs...",
    "icon_links": [
        {
            "url": "https://github.com/pymc-devs/pymc",
            "icon": "fa-brands fa-github",
            "name": "GitHub",
        },
    ],
}
html_context = {
    "github_user": "pymc-devs",
    "github_repo": "pymc",
    "github_version": "main",
    "doc_path": "docs/source/",
    "default_mode": "light",
}

# Add any paths that contain custom themes here, relative to this directory.
# html_theme_path = []

# The name for this set of Sphinx documents.  If None, it defaults to
# "<project> v<release> documentation".
# html_title = None

# A shorter title for the navigation bar.  Default is the same as html_title.
# html_short_title = None

# The name of an image file (relative to this directory) to place at the top
# of the sidebar.
html_logo = "../logos/PyMC.jpg"

# The name of an image file (within the static path) to use as favicon of the
# docs.  This file should be a Windows icon file (.ico) being 16x16 or 32x32
# pixels large.
html_favicon = "../logos/PyMC.ico"

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ["../logos"]

# Add any extra paths that contain custom files (such as robots.txt or
# .htaccess) here, relative to this directory. These files are copied
# directly to the root of the documentation.
# html_extra_path = []

# If not '', a 'Last updated on:' timestamp is inserted at every page bottom,
# using the given strftime format.
# html_last_updated_fmt = '%b %d, %Y'

# If true, SmartyPants will be used to convert quotes and dashes to
# typographically correct entities.
# html_use_smartypants = True

# Custom sidebar templates, maps document names to template names.

# Additional templates that should be rendered to pages, maps page names to
# template names.
# html_additional_pages = {}

# If false, no module index is generated.
# html_domain_indices = True

# If false, no index is generated.
# html_use_index = True

# If true, the index is split into individual pages for each letter.
# html_split_index = False

# If true, links to the reST sources are added to the pages.
# html_show_sourcelink = True

# If true, "Created using Sphinx" is shown in the HTML footer. Default is True.
# html_show_sphinx = True

# If true, "(C) Copyright ..." is shown in the HTML footer. Default is True.
# html_show_copyright = True

# If true, an OpenSearch description file will be output, and all pages will
# contain a <link> tag referring to it.  The value of this option must be the
# base URL from which the finished HTML is served.
# html_use_opensearch = ''

# This is the file name suffix for HTML files (e.g. ".xhtml").
# html_file_suffix = None

# Language to be used for generating the HTML full-text search index.
# Sphinx supports the following languages:
#   'da', 'de', 'en', 'es', 'fi', 'fr', 'h', 'it', 'ja'
#   'nl', 'no', 'pt', 'ro', 'r', 'sv', 'tr'
# html_search_language = 'en'

# A dictionary with options for the search language support, empty by default.
# Now only 'ja' uses this config value
# html_search_options = {'type': 'default'}

# The name of a javascript file (relative to the configuration directory) that
# implements a search results scorer. If empty, the default will be used.
# html_search_scorer = 'scorer.js'

# Output file base name for HTML help builder.
htmlhelp_basename = "pymcdoc"

# -- Options for LaTeX output ---------------------------------------------

latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    #'papersize': 'letterpaper',
    # The font size ('10pt', '11pt' or '12pt').
    #'pointsize': '10pt',
    # Additional stuff for the LaTeX preamble.
    #'preamble': '',
    # Latex figure (float) alignment
    #'figure_align': 'htbp',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [(master_doc, "pymc.tex", "PyMC Documentation", "PyMC developers", "manual")]

# The name of an image file (relative to this directory) to place at the top of
# the title page.
# latex_logo = None

# For "manual" documents, if this is true, then toplevel headings are parts,
# not chapters.
# latex_use_parts = False

# If true, show page references after internal links.
# latex_show_pagerefs = False

# If true, show URL addresses after external links.
# latex_show_urls = False

# Documents to append as an appendix to all manuals.
# latex_appendices = []

# If false, no module index is generated.
# latex_domain_indices = True


# -- Options for manual page output ---------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [(master_doc, "pymc", "pymc Documentation", [author], 1)]

# If true, show URL addresses after external links.
# man_show_urls = False


# -- Options for Texinfo output -------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (
        master_doc,
        "pymc",
        "pymc Documentation",
        author,
        "pymc",
        "One line description of project.",
        "Miscellaneous",
    )
]

# Documents to append as an appendix to all manuals.
# texinfo_appendices = []

# If false, no module index is generated.
# texinfo_domain_indices = True

# How to display URL addresses: 'footnote', 'no', or 'inline'.
# texinfo_show_urls = 'footnote'

# If true, do not generate a @detailmenu in the "Top" node's menu.
# texinfo_no_detailmenu = False


# def setup(app):
#     app.add_css_file("https://cdn.jsdelivr.net/npm/semantic-ui@2.4.2/dist/semantic.min.css")
#     app.add_css_file("default.css")
