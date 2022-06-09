# Lab 6: Writing to Kafka with code

### Disclaimer

In the final version here on GitHub, we use `data/sample.csv` instead of `data/twcs.csv` because of file size constraints. In the report below, everything is demonstrated using `data/twcs.csv`.

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
