# tvhm3u

**author:** Gian Luca Fiasco  
**mail:** glf@lucacloud.info

A simple frontend to tvh channel.m3u to support authentication

Many IPTV app on android don't support TVHEADEND Top Level BasicAuth but requires in line perChannel Auth

this service list on port 7878 and rewrite the TVH m3u playlist in a format supported by IPTV apps

# systemd service configuration

```
$ sudo cp tvhProxy.service /etc/systemd/system/TVHm3u.service
$ sudo systemctl daemon-reload
$ sudo systemctl enable TVHm3u.service
$ sudo systemctl start TVHm3u.service
```