### Installation and Execution

1. Run the following command to make the `install.sh` script executable and install dependencies:

   This script installs the required dependencies, including ffmpeg and shaka packager.

   ```bash
   chmod +x install.sh && ./install.sh
   ```

## Step 2: Configure Encryption Parameters

Ensure you have set the required variables in the `config.json` file. Open the `config.json` file and replace the placeholder values with your actual organization code, content ID, Widevine AES key, Widevine IV, and video path:

```json
{
  "org_code": "your_org_code",
  "content_id": "your_content_id",
  "widevine_aes_key": "your_widevine_aes_key",
  "widevine_iv": "your_widevine_iv",
  "video_path": "input.mp4"
}
```

## Step 3: Run Widevine Packager Script

Run the `widevine_packager.sh` script using the following commands:

```bash
chmod +x widevine_packager.sh && ./widevine_packager.sh
```


Upon successful execution, you should see the following message:

```bash
Packaging completed successfully.
```

You will find the generated MPD file (h264.mpd) in the current working directory.



## Step 4: Generate License URL

Run the `get_license_url.py` script to generate your license URL. Use the following command:

```bash
python3 get_license_url.py
```

You will receive your license URL in the following format:

```
License URL: https://app.tpstreams.com/api/v1/69xt46/drm_license/?data=eyJjb250ZW50X2RhdGEiOiJleUpqYjI1MFpXNTBYMmxrSWpvaVpHUmtaREZrWVdVNE9EWXlORE5pWlRnMU56RTJZekZtWWpnNE9UVTJORFVpTENKa2NtMWZkSGx3WlNJNkluZHBaR1YyYVc1bElpd2laRzkzYm14dllXUWlPbVpoYkhObGZRPT0iLCJzaWduYXR1cmUiOiI5QkM5aTloTFVMWHlmaXlBdXE5aHRhRGZYb3FRam9PWGtDOWlVbGd5Z3R3PSJ9
```
The `get_license_url.py` script internally calls two methods, `get_encoded_content_data` and `generate_signature`, both of which are required to generate the license URL. Ensure you've run these steps before generating the license URL.


## Step 5: Play the Video in Player

1. Copy the generated license URL and the path to the MPD (Media Presentation Description) file.
2. Open the `index.html` file.
3. Replace the placeholder values in the `player.src` section with your license URL and MPD file path.
4. Save the changes.

Now, to view the video, follow these steps:

1. Open a terminal.
2. Navigate to the directory containing your modified `index.html` file.
3. Run the following command to start a local server:

    ```bash
    python -m http.server
    ```

4. Visit [http://localhost:8000/index.html](http://localhost:8000/index.html) in your web browser.

You should now be able to play the video using the configured DRM settings and the provided license URL. If any issues occur, ensure that the MPD file path and license URL are correctly set in the `index.html` file.

To add step 6 to your instructions, you can follow these guidelines:


## Step 6: Get FairPlay URI, Key, and IV to Encrypt the Video with FairPlay DRM


1. Run the following command to execute the script:

    ```bash
    python3 get_key_iv_and_uri.py
    ```
    This script will send a POST request to the URL `https://app.tpstreams.com/api/v1/{org_code}/fairplay_key/` and obtain the FairPlay URI, Key, and IV
   
2. You will receive a response similar to the following:

    ```plaintext
    Response: b'{"iv":"c60e93703a0c423696b9dfa0e02b60d2","key":"a8031c8ba7474846b137ffc328cf2304","uri":"skd://4a961191b7764338b8a6ca3259023c2d"}'
    ```

3. Update the values of FairPlay URI, Key, and IV in `config.json` provided in the response
