# Splitfqdn
Split an FQDN in parts and rearrange its parts

# Usage
```
usage: splitfqdn [-h] [-321] format

positional arguments:
  format              %1 to %9 is replaced with the corresponding domain level
                      taken from the input (takes vTLD such as co.uk into
                      account). For example, if the argument %3.%2.%1 is given
                      and stdin supplies sub5.sub4.sub3.example.co.uk then
                      sub3.example.co.uk is returned. The dots are free-form,
                      any character can be used.

optional arguments:
  -h, --help          show this help message and exit
  -321, --extract321  Separeate second (%2) and top level domain (%1), and the
                      remaining part (%3).
```
# Example

```
echo www1.www2.google.co.uk | splitfqdn "%3 is the third level domain of %2.%1"
```
This results in:
```
www is the third level domain of google.co.uk
```
But using the -321 option, everything under the second level domain is return by %3:
```
echo www1.www2.google.co.uk | splitfqdn "%3 is the full subdomain of %2.%1" -321
```
This results in:
```
www1.www2 is the full subdomain of google.co.uk
```
