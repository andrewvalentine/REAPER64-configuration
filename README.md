# REAPER64 configuration

This repository provides the materials required to build a package to install a script that configures REAPER64.

I'm a Python novice, so much of the credit here goes to Stack Overflow and Tim Sutton on the #MacAdmins Slack Team.

## Notes

* This package delivers a script that is intended to be run at login via [Outset](https://github.com/chilcote/outset). If you are not using Outset, you will need to determine an alternative method of running login scripts as the authenticating user.
* By default, the included `Makefile` will attempt to sign your pkg or product. If you do not want to do so or do not have a Developer Certificate, you should remove the `productsign` invocations from the `Makefile`.
* This package takes the following configuration steps via `pkgroot/REAPER64-configuration.py`:
  * Disables automatic update checks
  * Hides licensing information in the title bar of the application
  * If these setting are undesirable or you wish to add further configuration, you will need to edit `pkgroot/REAPER64-configuration.py`.

## Usage

#### Essential:
* Edit the variables in `Makefile` as appropriate for your organisation.  I recommend reviewing the following:
  * `PKGTITLE`
  * `PKGVERSION`
  * `PKGID`
  * `SIGNINGID` - As above, this is only required if you are using a Developer ID to sign your pkgs. If you do not have a Developer ID, you will need to remove the `productsign` invocations from the `pkg` and `product` commands.


#### Optional:
* Configure `pkgroot/REAPER64-configuration.py` to add any desired settings you obtain from a configured installation of REAPER64. You can find client settings in:

```
~/Library/Application Support/REAPER/reaper.ini
```

* Build the pkg:

```
make pkg
```

* The resulting pkg will be delivered to `./output/$PKGTITLE.pkg`. You should then distribute this via your software deployment tool.
