# GF4: Structure from Motion

## Next Sessions
- 18 May: JDB Seminar Room
- 21 May: LR 11
## Compulsory Sessions

- Thursdays 9-11am
- Mondays 11-1pm


## Project Groups

- Group 1: F. Ganzer (fg442), Y. Pu (yp299), S.K. Pal (skp58)
- Group 2: M. Fylpchuk (mf818), T. Owen (to353), S. Sivaraya (ss3114)
- Group 3: Y. Wei (ytw25), N.Y. Ouis (nyo21), S. Li (sl2192)
- Group 4: E. Gu (eg685), V. Leoutsakos (vl346), J. Chen (jc2474)
- Group 5: Y-H. Liu (yhl63), R. Ivanchuk (ri302), J. Parimi (jp2057)
- Group 6: J. Everett (je477), H.J. Dalton (hd504), T.I.H. Hawkins (th706)

## Objectives

By the end of the course, students should be able to:

- understand the principles of Structure from Motion (SfM), one of the most important algorithms in computer vision, through hands-on experimentation and implementation
- explain the role of feature detection, feature matching, and camera pose estimation in an SfM pipeline
- use a professional SfM tool such as COLMAP to reconstruct sparse 3D structure and camera poses from a set of images
- design and analyse image-capture strategies for successful 3D reconstruction
- implement key components of a simplified SfM pipeline in Python

## Content

The aim of this project is to understand Structure from Motion through a combination of professional tools, mathematical foundations, and hands-on implementation. Structure from Motion is the process of recovering both the 3D structure of a scene and camera parameters from multiple overlapping images.

The project begins by treating COLMAP as a professional reference system. Students run COLMAP on both standard datasets and their own captured image sets, producing sparse reconstructions and visualising estimated camera poses and 3D point clouds. They perform controlled capture experiments to understand when SfM succeeds or fails, for example by varying the number of images, image overlap, texture, lighting, and camera motion. They also inspect intermediate outputs such as detected keypoints and matched image pairs.

Students then implement and analyse key steps of a simplified SfM pipeline in Python, including feature detection, descriptor matching, and relative pose recovery. Modular utilities are provided so that the focus remains on understanding and experimentation rather than low-level software infrastructure.

The project culminates in a short group presentation and an individual final report, showcasing the reconstruction pipeline, visual results, quantitative and qualitative analysis, and lessons learned about the strengths and limitations of Structure from Motion.

## Weekly Plan

### Week 1

- setting up the Python and COLMAP environment and running COLMAP sparse reconstruction
- visualising sparse point clouds and estimated camera poses
- creating controlled ablations, such as fewer images, lower overlap, poor texture, or challenging lighting
- reading introductory material on multiview geometry and SfM
- detailed guide: [week1/README.md](week1/README.md)

### Week 2

- extracting descriptors
- matching descriptors between image pairs
- estimating the fundamental matrix

### Week 3

- recovering relative camera rotation and translation
- triangulating sparse 3D points
- visualising reconstructed sparse points and camera poses

### Week 4

- analysing failure cases
- preparing and delivering final presentation and report

## Coursework

| Coursework | Due Date | Marks |
|---|---|---|
| Interim Report 1 | 21 May 2026 | 15 (individual) |
| Interim Report 2 | 28 May 2026 | 15 (individual) |
| SfM code and Presentation | 11 June 2026 | 30 (group) |
| Final Report | 11 June 2026 | 40 (individual) |
