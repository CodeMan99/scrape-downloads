1. `npm install` the dependancies in "package.json".
2. Create a folder in which to store the HTML documents.
3. Create a folder in which to store the files.
4. Open Chrome's network inspector (dev tools). Check "Preserve Log".
5. Navigate to the page being scraped.
6. Right click on the files page network request, click on "Copy as cURL".
7. Paste the command into a file called "curl-template.sh".
    1. Add the `-L` flag at the start for redirects.
    2. Replace the "pathname" part of the request url with `{href}`.
    3. Add `-o '{filename}'` to the end of the command.
8. Wrap it up by running the tools. Below is an example.

    ```bash
    $ ./write-get-pages-sh.py 14
    $ pushd pages && ../get-pages.sh && popd
    $ ./scrape.js pages | ./write-curl-sh.py
    $ pushd files && ../download.sh && popd
    $ zip --encrypt somefilename.zip files/*
    ```
