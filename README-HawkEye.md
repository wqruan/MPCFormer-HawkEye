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

After running the following commands, `log_mpcformer_online.txt` would contain the online communication size, online communication round, and running time results from MPCFomer shown in Table 2, Table 3, and Figure 7 of the paper "HawkEye: Statically and Accurately Profiling the Communication Cost of Models in Multi-party Learning" (Usenix Security 2025). It takes about ten minutes. The online communication size/round number of "Matmul" CrypTen operator is the sum of communication size/round number of "ËmbedCommByte"/"ËmbedRound" and "LinearCommByte''/"LinearRounds" in log_mpcformer_online.txt. The online communication size/round number of "Gelu" operator is "ActCommByte"/"ActRounds" in log_mpcformer_online.txt. The online communication size/round number of "Softmax" operator is "SoftmaxCommByte"/"SoftmaxRounds" in log_mpcformer_online.txt. For the offline communication size of CrypTen operators in Table 2, you can first compute the total communication size according to log_mpcformer_online+offline.txt. Then the offline communication size of operators can be obtained by subtracting the online communication size from the communication size. Besides, the unit of "ËmbedCommByte", "LinearCommByte'', "ActCommByte", "SoftmaxCommByte" is byte.

```
cd src/benchmark/
chmod +x run_online.sh
./run_online.sh
```


After running the following commands, `log_mpcformer_online+offline.txt` will contain the total communication size results from MPCFomer. The offline communication size results shown in Table 2 can be obtained by subtracting the online communication size results from the total communication size results. It takes about ten minutes. The offline communication size of operators can be obtained through similar methods to the online communication size.

```
chmod +x run_online+offline.sh
./run_online+offline.sh
```
