To run CLI:
`python bomdotcom.py`
Must be run with Python 3.5 or above

First input provided should be the number of MPNs desired from BOM
Subsequent inputs are the BOM lines describing MPNs

MPN are expected in one of 3 formats:
    Format 1:
       MPN:Manufacturer:ReferenceDesignators
       (e.g. TSR-1002:Panasonic:A1,D2)
    Format 2:
       Manufacturer -- MPN:ReferenceDesignators
       (e.g. Panasonic -- TSR-1002:A1)
    Format 3:
       ReferenceDesignators;MPN;Manufacturer
       (e.g. A1,B2,C8;TSR-1002;Keystone)

Any MPN line which doesn't match one of the above formats will be ignored

To add support for a new BOM line format, add its regex to the `REGS` array in `bomdotcom.py`, and add a corresponding test to `test.py`

To run tests, `python test.py`

Assumptions:
    MPN (Model Part Number) consists of alphanumeric characters and hyphens only.
    Manufacturer and Reference Designators consists of alphanumeric characters only.
    Order does not matter in reference designators list. If it did, special care would have to be added when unioning two lists of reference designators for 2 or more BOM lines with the same MPN and Manufacturer.
