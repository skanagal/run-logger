# Example - Running the script directly from CLI

After saving the script on flash drive.

Create an alias on CLI:

```
alias field_set_refresh bash setsid python /mnt/flash/run-logger.py %1 %2
```

```
pe1-ghb265#field_set_refresh 567 ipv6
pe1-ghb265#
```

Note: setsid kickstarts the script in the background.

## Logs should have been generated:

```
Mar 18 07:31:23 pe1-ghb265 run-logger.py: 7685  Started collecting output.
Mar 18 07:31:24 pe1-ghb265 run-logger.py: 7685  Finished collecting the output.

```


# Example - Running the script from remote machine which uses SSH to interact with EOS

You can use a the run-remote-cmds.py script to run the alias command. The script will automatically configure alias if it does not exist already.

```

sureshk@sureshk run-logger % python run-remote-cmds.py 7686 ipv6
sureshk@sureshk run-logger %

```
Logs:

```
Mar 18 07:36:08 pe1-ghb265 run-logger.py: 7686  Started collecting output.
Mar 18 07:36:10 pe1-ghb265 run-logger.py: 7686  Finished collecting the output.
```
