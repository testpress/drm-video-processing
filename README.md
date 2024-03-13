### Installation and Execution

1. Run the following command to make the `install.sh` script executable and install dependencies:

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
