### lama

a linux/mac app to take screenshots and upload to imgur.


#### installation


```bash
$ (sudo) pip install lama
```

#### usage

get your client id from <a href='http://api.imgur.com/'>imgur api</a> and create a config file named `.imgur.conf` in your user's
directory. 

there is an example preformatted config file in the repository:
```bash
$ wget https://raw.github.com/emre/lama/master/extras/.imgur.conf -O ~/.imgur.conf
```

```ini
[client]
id = YOUR_CLIENT_ID
```

**running**

```bash
$ lama
```

or `ALT+F2` and `lama`


#### how it works

All of your screenshots will be in your  `~/imgur_uploads` directory as a backup on the disk.


| platform      | action          |     system call   |
| ------------- |---------------| ------------------------------|
| linux         | taking shot   | scrot                                       |
| mac           | taking shot    | screencapture     |
| linux         | notifications  | notify-send                                       |
| mac           | notifications    | afplay /System/Library/Sounds/Glass.aiff     |
| linux         | clipboard operations  | xsel                                       |
| mac           | clipboard operations   | pbcopy     |

**Note:** <a href="http://en.wikipedia.org/wiki/Scrot">scrot</a> and <a href="http://www.vergenet.net/~conrad/software/xsel/">xsel</a> must be installed for linux users. 
