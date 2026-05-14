# GF4 Structure from Motion — Week 1 Guide
## Empirical Study of Sparse SfM with COLMAP

## Report templates

- Overleaf template: https://www.overleaf.com/read/jzfdccmknccp#17a7ee

**Goal:** Use COLMAP as a professional reference system to understand what sparse Structure from Motion produces and what image-capture conditions make it succeed or fail.  
**Main deliverable:** A structured intermediate report analysis COLMAP sparse reconstructions, camera-pose visualisations, feature/match inspection, controlled capture experiments, and explanations of success/failure.

You should treat COLMAP as a black-box engineering system and investigate it systematically.

---

## Week 1 learning objectives

By the end of Week 1, you should be able to:

1. Run COLMAP sparse reconstruction on a small image collection.
2. Interpret the key COLMAP sparse SfM outputs:
   - registered images,
   - sparse 3D points,
   - camera poses / camera trajectory,
   - feature and match information.
3. Design a good image capture for SfM.
4. Explain why some captures reconstruct successfully while others fail.
5. Inspect detected features and matched image pairs using COLMAP tools.
6. Produce a concise evidence-based comparison across several datasets.

COLMAP dense stereo usually requires a CUDA-enabled NVIDIA GPU, which many laptops do not have. We will only focus on sparse reconstruction.

---

## Required reading

Read the following before the second session:

Antonio Torralba, Phillip Isola, and William T. Freeman,  
*Foundations of Computer Vision*, Chapter 44:  
**“Multiview Geometry and Structure from Motion”**  
https://visionbook.mit.edu/multiview.html


Main idea:

> How can multiple 2D images of the same static scene be used to recover both 3D structure and camera motion?

Questions to answer as you read:

1. Why multiple views contain more 3D information than a single image.
2. Why matching or tracking points across images is central to SfM.
3. What assumptions make SfM possible, especially static-scene assumption.
4. How the reading connects to the sparse points and camera poses produced by COLMAP.

---

## Required software


You should use **conda** and **Python 3.10+**: https://docs.anaconda.com/miniconda/.

You must also install 
- **COLMAP** with GUI support: https://colmap.github.io/install.html.
- pycolmap with pip: https://pypi.org/project/pycolmap/.

---

## Phase A — Run COLMAP

Open COLMAP and verify that the GUI launches:

```bash
colmap gui
```
Download the "South Building" dataset from:

https://colmap.github.io/datasets.html

Run COLMAP sparse reconstruction on this dataset.
### Create a project folder

Use a separate folder for each reconstruction:

```text
week1/south_building/
  images/
  database.db
  sparse/
```

Copy the images into `images/`.

### Create a new project

In COLMAP:

```text
File → New project
```

Set:

```text
Database:     week1/south_building/database.db
Image folder: week1/south_building/images/
```
### Feature extraction

```text
Processing → Feature extraction
```

Recommended initial settings:

```text
Camera model: SIMPLE_RADIAL
Single camera: enabled if all images use the same camera
Use GPU: enabled if available; disabled if GPU causes problems
```

### Feature matching

For datasets with fewer than a few hundred images, use:

```text
Processing → Feature matching → Exhaustive matching
```

Sequential matching is only recommended for long video-like sequences with correct temporal ordering.

### Sparse reconstruction

```text
Reconstruction → Start reconstruction
```

After reconstruction, record:

```text
Number of input images:
Number of registered images:
Number of sparse 3D points:
Whether camera poses look plausible:
Whether the point cloud resembles the object/scene:
```

### Expected output

For a good dataset, you should normally see:

- most or all images registered,
- a visible sparse point cloud,
- camera frustums arranged plausibly around the object/scene.

Exact numbers may differ by machine and COLMAP version.

### If it does not work

Use this debugging order:

1. Does COLMAP open?
2. Can COLMAP import the images?
3. Does feature extraction complete?
4. Does feature matching complete?
5. Does sparse reconstruction register at least two images?
6. Does the viewer show sparse points and cameras?

If COLMAP says reconstruction is complete but the viewer is empty, check the log for messages such as:

```text
No good initial image pair found
Discarding reconstruction due to bad initial pair
```

This usually means that COLMAP found too few geometrically reliable image pairs, or that the available pairs lacked sufficient parallax.

### Also run the Python workflow (pycolmap)

After completing the GUI workflow above, run the Week 1 Python script as a second method.
This helps you compare GUI-based and script-based reconstruction workflows.

From the workspace root, run:

```bash
conda run -n gf4-sfm python GF4/week1/test.py \
   --image-dir path_to_image_folder \
   --output-dir path_to_output_folder \
   --threads 2 \
```
You should be comfortable with both GUI and python implementations. You can choose either for the next experiments.

---


## Phase B — Systematic data acquisition experiment

You will capture your own image sets for a single object or small static scene.




### Capture protocol

Create multiple image sets. You will likely need to make multiple attempts for each set.

#### Set 1: Good-quality capture

- 60-100 images.
- Keep the object/scene static.
- Avoid motion blur.
- Avoid large exposure changes.
- Avoid zoom changes.

Choose something with:

- good texture,
- non-reflective surfaces,
- stable lighting,
- no moving objects,
- enough 3D structure.

Good choices:

- a textured sculpture,
- a pile of books,
- a chair with textured surroundings,
- a building façade with distinctive features,
- an engineering object with labels/texture.

Bad first choices:

- shiny metal object,
- glass,
- a mirror,
- a blank wall,
- a moving person,
- an object on a rotating turntable unless explicitly analysed as a failure case.
#### Set 2: Minimal/subsampled capture

- up to 15-20 images of the same object/scene

#### Set 3: Challenging/failure capture

Choose **three** challenges:

- low light,
- motion blur,
- shiny/specular surface,
- textureless surface,
- repeated pattern,
- low overlap,
- object moved between shots,
- camera mostly rotating in place with little translation.


---

## Phase C — Run COLMAP on your captures

Run COLMAP sparse reconstruction on:

1. your best capture,
2. your minimal/subsampled capture,
3. your challenging/failure captures.


COLMAP does not only produce a final reconstruction. It also stores intermediate feature and matching information.

Open:

```text
Processing → Manage database
```

For at least two datasets: your best capture and one challenging/failure capture, inspect:

1. detected keypoints in one representative image
2. overlapping/matched image pairs



---

## Intermediate Report

Submit an individual report, max **4 pages**, containing:

Practical work is performed in groups of 3, but each student must submit their own report with their own interpretation and analysis.

1. **Answer the following questions briefly (2-3 sentences):**
   - Why do multiple views contain more 3D information than a single image?
   - Why are matching and tracking points across images central to SfM?
   - Why is a static scene assumption necessary?

2. **COLMAP reconstruction results on the South Building Dataset**
   - sparse point-cloud screenshots
   - camera-pose screenshots

3. **Description of your scenes**
   - Why did you choose the scenes?
   - What makes the easy capture easy and the challenging capture challenging?


4. **Your results**

   For each set, record:

   | Quantity | Meaning |
   |---|---|
   | number of input images | How many images you provided |
   | number of registered images | How many images COLMAP successfully used |
   | number of sparse points | approximate sparse reconstruction size |
   | camera poses plausible? | yes / partial / no |
   | qualitative quality | good / partial / poor / failed |
   | main observed failure | your diagnosis and analysis |


   Create a table like this:

   | Dataset | Input images | Registered images | Sparse points | Camera poses plausible? | Main observation |
   |---|---:|---:|---:|---|---|
   | Best capture | | | | | |
   | Minimal/subsampled | | | | | |
   | Challenging/failure (3 rows) | | | | | |

   
   - For each scene, include visualizations of the feature matches, recovered camera poses, and the 3D reconstruction.

5. **Analysis**
   - What made SfM work when it worked?
   - What made it fail when it failed?

   Refer to results from the previous section to support your arguments.

6. **Group Dynamics**
   - Briefly describe the contribution of each member in your group (max 2-3 sentences per person)

---
