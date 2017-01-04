# Socket Speed

After reading [How fast are Unix domain sockets?](https://blog.myhro.info/2017/01/how-fast-are-unix-domain-sockets) I started wondering about a lesser known Unix socket feature: abstract namespaces.

[The Linux Programming Interface](http://man7.org/tlpi/) defines abstract socket namespaces as:

> 57.6 The Linux Abstract Socket Namespace
>
> The so-called abstract namespace is a Linux-specific feature that allows us to bind a UNIX domain socket to a name without that name being created in the file system. This provides a few potential advantages:
>
> * We don’t need to worry about possible collisions with existing names in the file system.
> * It is not necessary to unlink the socket pathname when we have finished using the socket. The abstract name is automatically removed when the socket is closed.
> * We don’t need to create a file-system pathname for the socket. This may be useful in a chroot environment, or if we don’t have write access to a file system.
>
> To create an abstract binding, we specify the first byte of the `sun_path` field as a null byte (\0).
> [...]

In addition to IP sockets and Unix domain sockets, I've added a test client/server for abstract namespace sockets. As it turns out, abstract namespace sockets are actually a bit faster. The difference is not as noticeable as IP socket -> Unix domain socket, but it's there.

IP sockets:

```
$ python3 ip_client.py
Receiving messages...
Received 16254 messages in 1 second(s).
```

Unix domain sockets:

```
$ python3 uds_client.py
Receiving messages...
Received 41654 messages in 1 second(s).
```

Abstract namespace sockets:

```
$ python3 ans_client.py
Receiving messages...
Received 43539 messages in 1 second(s).
```

Abstract namespace sockets weren't specifically created with performance in mind, but hey, I'll take a free speed boost when I can get it.
