# SatVision: GUI Map Viewer - Backend

- Backend workflows for SatVision's real-time satellite image and land cover segmentation renderer. 
- Deploys the novel **`patchify-process-reconstruct`** approach to run DL-driven segmentation inference in real-time.
- Flask REST API endpoints callable by cross-platform frontend frameworks; Implementation tested with [Mapbox](https://www.mapbox.com/).

## High-level Organization of the API

- API endpoint definitions are contained in [api](./api).
- Corresponding tests are packaged in [api-tests](./api-tests).
- [fetcher](./api/fetcher) packages callables to fetch real-time satellite data from [Sentinel-Hub](./https://www.sentinel-hub.com/).
  - API tokens for Sentinel-Hub will need renewal.
  - Session management wrappers are defined as callables for token-based OAuth with Sentinel-Hub ([specific details here](https://github.com/SIH-22-Kyogre/SatVision_Satellite-Image-Acquisition)).
- Utilities and patch-wise processing workflows are also defined as API endpoints, for allowing tailored image processing workflows.
