# Lab 6: Writing to Kafka with code

### Disclaimer

`data/twcs.csv` was not uploaded due to its large size. Download it to replicate the results.

### Report

Running the cluster still looks the same as in the previous lab:

![running cluster](screenshots/run-cluster.jpg)

Of course, to shut it down you can run `shutdown-cluster.sh`.

---

With `build_sender.sh` you can buld and run the producer program.

![container launch](screenshots/container-launch.jpg)

---

Finally, the output from the console consumer client is correct:

![consumer outputs](screenshots/consumer-output.jpg)

And leaving it up for ~5 minutes doesn't break it.

![after 5 minutes](screenshots/after-5-minutes.jpg)
