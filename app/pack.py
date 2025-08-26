from stlitepack import pack, setup_github_pages
from stlitepack.pack import get_stlite_versions, list_files_in_folders

# get_stlite_versions()

pack(
    "launch.py",
    requirements=["plotly", "vidigi==0.0.4", "seaborn", "sim-tools"],
    extra_files_to_embed=[
        "animation.py",
        "home_page.py",
        "model.py",
        "more_info_page.py",
        "sim_page.py"
        ],
    extra_files_to_link=[
        "img/model_diagram.jpg",
        "img/model_diagram.png",
        "sq8.png"
    ],
    prepend_github_path="bergam0t/hr_non-elective-flow-simulation",
    output_dir="..",
    use_raw_api=True
    )

setup_github_pages(mode="gh-actions", output_dir="..", use_docs=False)
