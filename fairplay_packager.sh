# Read configuration from config.json
JSON_FILE="config.json"
CONTENT_ID=$(jq -r '.content_id' "$JSON_FILE")
VIDEO_PATH=$(jq -r '.video_path' "$JSON_FILE")
FAIRPLAY_KEY=$(jq -r '.fairplay_key' "$JSON_FILE")
FAIRPLAY_IV=$(jq -r '.fairplay_iv' "$JSON_FILE")
FAIRPLAY_URI=$(jq -r '.fairplay_uri' "$JSON_FILE")



# Execute packager command
packager -v=4 \
  in="${VIDEO_PATH},stream=audio,output=static/audio.mp4" \
  in="${VIDEO_PATH},stream=video,output=static/h264_360p.mp4" \
  --enable_raw_key_encryption \
  --keys "label=:key_id=${CONTENT_ID}:key=${FAIRPLAY_KEY}:iv=${FAIRPLAY_IV}" \
  --protection_scheme cbcs \
  --protection_systems Fairplay \
  --hls_key_uri "$FAIRPLAY_URI" \
  --clear_lead 0 \
  --hls_master_playlist_output static/video.m3u8
