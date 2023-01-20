# Proxy Workflows sketch

This folder contains an example workflow, that demonstrates how
OpenAssetIO's `getRelatedReferences` can be used to query alternate
representations of an image sequence. Either in the form of the
"original" version, or some proxy representation.

This workflow could be used to rebuild an EDL with alternate versions,
for example, a multi-ref OTIO file.


## Setup

Assuming linux/macOS, and the working directory is a checkout of this
codebase.


```shell
# Make a venv as this is all heavily experimental
python -m venv .venv
. ./.venv/bin/activate

# Install MediaCreation itself
python -m pip install .

# Install the requirements of the sketch
python -m pip install -r examples/proxy_workflows/requirements.txt
```

If you now switch the example directory we can make use of the included
sample data.

```shell
cd examples/proxy_workflows

# Tell OpenAssetIO to use the preconfigured BAL library
export OPENASSETIO_DEFAULT_CONFIG=bal_proxies_openassetio_config.toml
```

## Usage

The sketch models a contrived workflow, whereby you provide it with a
single entity reference, and it queries any alternate image sequence
representations. Any discovered references are printed out to the shell.

The included BAL library is very simple. It contains some footage from
on set.

- `bal:///plate/original`

The plate has three proxy alternatives of different sizes:

 - `bal:///plate/proxy/1080`
 - `bal:///plate/proxy/720`
 - `bal:///plate/proxy/576`

You can use the script with any of these references to explore the
available alternatives, eg:

```shell
python ./proxies.py bal:///plate/proxy/1080
```

This should show you info about the orginal, as well as other available
proxies:

```shell
$ python ./proxies.py bal:///plate/proxy/1080
Representations for: bal:///plate/proxy/1080

Original:

bal:///plate/original
  - openassetio-mediacreation:content.LocatableContent:
      location: file:///media/plate.orig.%2504d.exr
  - openassetio-mediacreation:time.FrameRanged:
      startFrame: 1001
      endFrame: 1351
  - openassetio-mediacreation:image.Image
  - openassetio-mediacreation:image.OCIOColorManaged:
      colorspace: ADX10
  - openassetio-mediacreation:image.Raster:
      width: 4096
      height: 2160

Proxies:

 bal:///plate/proxy/720
  - openassetio-mediacreation:content.LocatableContent:
      location: file:///media/plate.720p.mov
  - openassetio-mediacreation:time.FrameRanged:
      startFrame: 1001
      endFrame: 1351
  - openassetio-mediacreation:image.Image
  - openassetio-mediacreation:image.OCIOColorManaged:
      colorspace: Rec.709-sRGB
  - openassetio-mediacreation:image.Raster:
      width: 1920
      height: 720
  - openassetio-mediacreation:representation.Proxy:
      label: Half HD (720p)
      scaleRatio: 0.333

 bal:///plate/proxy/576
  - openassetio-mediacreation:content.LocatableContent:
      location: file:///media/plate.PAL.mov
  - openassetio-mediacreation:time.FrameRanged:
      startFrame: 1001
      endFrame: 1351
  - openassetio-mediacreation:image.Image
  - openassetio-mediacreation:image.OCIOColorManaged:
      colorspace: Rec.709-sRGB
  - openassetio-mediacreation:image.Raster:
      width: 720
      pixelAspectRatio: 1.422
      height: 576
  - openassetio-mediacreation:representation.Proxy:
      label: PAL (anamorphic)
      scaleRatio: 0.267
```
