# tvhm3u

**author:** Gian Luca Fiasco  
**mail:** glf@lucacloud.info

A simple frontend to tvh channel.m3u to support authentication

Many IPTV app on android don't support TVHEADEND Top Level BasicAuth but requires in line perChannel Auth

the service list on port 7878 and rewrite the TVH m3u playlist in a format supported by IPTV apps

# What's for

This daemon should run aside your tvheadend daemon and both port should be exposed to the internet:

- tcp 9981 (or else) for TVHEADEND
- tcp 7878 (or else) for TVHm3u

Android Clients IPTV App should set the url of the playlist to `http://IP:7878/playlist&token=TOKEN`

TOKEN can be set as system environment otherwise is generated and displayed in the logs

# systemd service configuration

```
sudo cp TVHm3u.service /etc/systemd/system/TVHm3u.service
sudo systemctl daemon-reload
sudo systemctl enable TVHm3u.service
sudo systemctl start TVHm3u.service
```

# Docker
see docker-compose.yaml for an example