# MPCFormer-Hawkeye

This README file describes how to reproduce the model communication cost profiling results from MPCFormer shown in Table 2, Table 3, and Figure 7 of the paper "HawkEye: Statically and Accurately Profiling the Communication Cost of Models in Multi-party Learning" (Usenix Security 2025).

## Build the environment

```
virtualenv venv --python 3.8
source venv/bin/activate
export SKLEARN_ALLOW_DEPRECATED_SKLEARN_PACKAGE_INSTALL=True
pip install -r requirements.txt
```

## Run profiling processes

After running the following commands, `log_mpcformer_online.txt` would contain the online communication size, online communication round, and running time results from MPCFomer shown in Table 2, Table 3, and Figure 7 of the paper "HawkEye: Statically and Accurately Profiling the Communication Cost of Models in Multi-party Learning" (Usenix Security 2025). It takes about ten minutes.

```
cd src/benchmark/
chmod +x run_online.sh
./run_online.sh
```


After running the following commands, `log_mpcformer_online+offline.txt` will contain the total communication size results from MPCFomer. The offline communication size results shown in Table 2 can be obtained by subtracting the online communication size results from the total communication size results. It takes about ten minutes.

```
chmod +x run_online+offline.sh
./run_online+offline.sh
```
