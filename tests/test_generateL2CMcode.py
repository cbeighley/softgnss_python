import pytest
from peregrine.include.generateL2CMcode import generateL2CMcode

end_shift_regs_test = [\
    0552566002,
    0034445034,
    0723443711,
    0511222013,
    0463055213,
    0667044524,
    0652322653,
    0505703344,
    0520302775,
    0244205506,
    0236174002,
    0654305531,
    0435070571,
    0630431251,
    0234043417,
    0535540745,
    0043056734,
    0731304103,
    0412120105,
    0365636111,
    0143324657,
    0110766462,
    0602405203,
    0177735650,
    0630177560,
    0653467107,
    0406576630,
    0221777100,
    0773266673,
    0100010710,
    0431037132,
    0624127475
]

def test_generateL2CMcode():
  for i in range(32):
    assert (end_shift_regs_test[i] == generateL2CMcode(i)[1])

