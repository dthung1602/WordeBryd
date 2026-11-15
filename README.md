# Worde Bryd

_Bring back WordBird from the grave_

<img src="./public/resources/screen-shot.png" alt="WordBird ScreenShot">

### How it works

Run a x86 emulator, boot a Windows 2000 image, and run WordBird from CD ISO file. All in browser.

Development

```shell
cd public && python3 -m http.server  # go to localhost:8000
```

Deployment

```shell
firebase deploy --only hosting
```

### Resources

- **Wordbird** ISO file from [archive.org](https://archive.org/details/wordbird)
- **V86 Emulator Lib** download from [Github Commit 315b2b0](https://github.com/copy/v86/releases/tag/latest)
- **Windows 2000 Image** download from [copy.sh](https://c.copy.sh/windows2k-v2)
    ```shell
    rm -rf public/resources/windows2000
    mkdir -p public/resources/windows2000
    python3 download_windows_img.py
    zstd -T8 -19 -r --progress --exclude-compressed public/resources/windows2000
    ```

### License

Code is under [MIT License](LICENSE)