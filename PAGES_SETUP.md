[stlitepack] Github Pages Workflow mode selected.

To complete setup:
1. Go to your repository **Settings -> Pages**.
2. Under "Build and deployment", set:
  - Source: **Github Actions**
3. Commit the following files:
  - the deploy.yml file that has been created in .github/workflows
  - the `index.html` and `.nojekyll` files that have been created in ..
4. Visit your deployed app at https://your-github-username.github.io/your-repo-name/
  - note that it may take a few minutes for the app to finish deploying
