#!/usr/bin/env python3

#電子情報通信学会誌　2024年9月号　Vol1.107, No.9, 2024
#p.863

#https://www2.yukawa.kyoto-u.ac.jp/~koudai.sugimoto/dokuwiki/doku.php?id=python:qiskit:%E3%82%A4%E3%83%B3%E3%82%B9%E3%83%88%E3%83%BC%E3%83%AB
#Qiskit1.1 kiroku

from qiskit import QuantumRegister, QuantumCircuit
from qiskit import BasicAer, execute

qr=QuantumRegister(2,"qr")
qc=QuantumCircuit(qr)

#量子回路の部分
qc.h(qr[0])
qc.cs(qr[0],qr[1])

#状態ベクトルを取得する
svsim=BasicAer.get_backend("statevector_simulator")
result=execute(qc,svsim).result()
statevector=result.get_statevector(qc)

print(statevector)

