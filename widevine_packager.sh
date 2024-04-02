# Read configuration from config.json
JSON_FILE="config.json"
ORG_CODE=$(jq -r '.org_code' "$JSON_FILE")
CONTENT_ID=$(jq -r '.content_id' "$JSON_FILE")
WIDEVINE_AES_KEY=$(jq -r '.widevine_aes_key' "$JSON_FILE")
WIDEVINE_IV=$(jq -r '.widevine_iv' "$JSON_FILE")
VIDEO_PATH=$(jq -r '.video_path' "$JSON_FILE")

# Execute packager command
packager \
  in="${VIDEO_PATH},stream=audio,output=static/audio.mp4" \
  in="${VIDEO_PATH},stream=video,output=static/h264_360p.mp4" \
  --enable_widevine_encryption \
  --signer testpress \
  --key_server_url https://app.tpstreams.com/api/v1/"$ORG_CODE"/widevine_key/ \
  --content_id "$CONTENT_ID" \
  --aes_signing_key "$WIDEVINE_AES_KEY" \
  --aes_signing_iv "$WIDEVINE_IV" \
  --mpd_output static/h264.mpd
