"""
To run this file, first make sure you have moved into the app subfolder!

This can be achieved by opening a terminal in the root of the repository, then running
`cd app`

You can then run this file with
`python -m pack`

or by using 'Run python file (in terminal)' in VSCode if that's your IDE.
"""

from stlitepack import pack, setup_github_pages
from stlitepack.pack import get_stlite_versions

# We first check what stlite versions are available to choose from. This prints a
# message in the terminal.
get_stlite_versions()

pack(
    # When we're in the app folder, this is our entrypoint (main) file - the one we'd run if
    # we were previewing our streamlit app with the command `streamlit run`
    app_file="launch.py",
    # we need to lock vidigi's version, but everything else can be flexible
    requirements=["plotly", "vidigi==0.0.4", "seaborn", "sim-tools"],
    # We embed the additional python files. Several of these are pages accessed by launch.py
    # as part of st.navigation
    extra_files_to_embed=[
        "animation.py",
        "home_page.py",
        "model.py",
        "more_info_page.py",
        "sim_page.py",
    ],
    # There are a few non-text files we're like to make sure we have access to
    extra_files_to_link=["img/model_diagram.jpg", "img/model_diagram.png", "sq8.png"],
    # The hosted files are stored in a particular repository - we pass this in in the format
    # username/repository_path
    prepend_github_path="bergam0t/hr_non-elective-flow-simulation",
    # In this case, we want our output index.html to be in the folder one level above our app
    # folder, so we pass ".." to tell it to move one level up
    output_dir="..",
    # The raw API is now the default option in v 0.4.0 of stlitepack and beyond
    # and is necessary to use for more complex features of stlitepack, like file linking
    use_raw_api=True,
    # stlitepack defaults to a slightly older version of stlite
    # We're going to request a version that's known to work particularly well (as versions either
    # side sometimes experience issues with either plotly plots displaying, or dataframes displaying)
    js_bundle_version="0.80.5",
    stylesheet_version="0.80.5",
    # We're experiencing an odd bug with dataframe display that is quite common - so we can
    # work around this by changing any dataframes to tables instead
    replace_df_with_table=False,
    # Finally, we'll request to run a preview server so we can display the created app
    run_preview_server=True,
)

# !! Note that because of the preview server being opened up,
# the next bit won't run until we close our preview server with CTRL + C !!

# We also want to create a workflow file to aid in deployment
setup_github_pages(
    # We want to deploy our site using github actions
    mode="gh-actions",
    # We are in the app subfolder, so we need to move up a level to the repository root
    # before we create the .github folder where our deployment workflow will sit
    root_dir="..",
    # We didn't put our output in the docs folder when packing as there was already a different set
    # of documentation files in there - so we specify use_docs = False so that the created workflow
    # file knows to look at the root of the repository
    use_docs=False,
    # Finally, we want the .nojekyll files to be created automatically to ensure no post-processing
    # of our index.html file happens when it's uploaded to github pages
    create_nojekyll=True,
)
