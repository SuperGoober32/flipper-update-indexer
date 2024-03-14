# Flipper Zero Update Indexer and Uploader

## Start locally
```bash
    INDEXER_FIRMWARE_GITHUB_TOKEN= \
    INDEXER_TOKEN= \
    make run
```

Clearing:
```bash
    make clean
```

## Requests example
Get index
```bash
    curl 127.0.0.1:8000/firmware/directory.json
```

Get latest release
```bash
    # format: 127.0.0.1:8000/{directory}/{channel}/{target}/{type}
    # if target contains '/' (slash) replace it by '-' dash symbol
    curl 127.0.0.1:8000/firmware/release/f7/updater_json
```

Trigger reindex
```bash
    curl -H "Token: YOUR_TOKEN" 127.0.0.1:8000/firmware/reindex
```

Upload files
```bash
    curl -L -H "Token: YOUR_TOKEN" \
        -F "branch=drunkbatya/test-spimemmanager" \
        -F "files=@flipper-z-any-core2_firmware-0.73.1.tgz" \
        -F "files=@flipper-z-f7-full-0.73.1.json" \
        127.0.0.1:8000/firmware/uploadfiles
```
