# GF4 Structure from Motion - Week 4 Guide
## Final Multi-View Reconstruction and COLMAP Comparison

**Goal:** Extend your Week 3 reconstruction from three images to one or more small multi-view systems, compare them with COLMAP on the same images, and prepare your final report and presentation.

This is the final project week. There is no new starter code. You have already built the main pieces: feature extraction, descriptor matching, geometric verification, two-view reconstruction, triangulation, PnP registration, reprojection checks, and visualisation. The Week 4 task is to connect these pieces into a small system and analyse what happens.

---

## Main task

Use your Week 2 and Week 3 code to attempt reconstruction on roughly **10** or more overlapping images. These may come from one image set or from multiple image sets. You should try to achieve high-quality reconstructions. 

You should:

- choose one or more image sets or subsets that are suitable for reconstruction,
- use your Week 2 evidence to choose a good initial pair,
- initialise a two-view reconstruction,
- extend from three images to a larger set using your own design choices,
- visualise the final registered cameras and sparse points,
- run COLMAP on the same images used for each reconstruction attempt,
- compare your system with COLMAP,
- use the results to prepare your final report and presentation.

---

## Creative room

You have freedom in how you extend the system. For example, you may decide:

- how to choose the next image to try,
- whether to triangulate new points after registering more images,
- how to visualise the final reconstruction,
- which failure cases to analyse,
- which image sets or datasets to use.

The important requirement is that your choices are explained and supported by evidence or arguments.

---

## Evidence to produce

By the end of Week 4, your group should have:

- at least one reconstruction attempt on roughly 10 or more images,
- quantitative evidence from your pipeline, such as PnP inliers, reprojection errors, number of registered cameras, and number of sparse points,
- qualitative evidence from your pipeline, such as camera-pose plots, sparse point visualisations, patch-cloud plots, or reprojection overlays,
- a COLMAP reconstruction on the same images for each main reconstruction attempt,
- quantitative and qualitative comparison with COLMAP,
- a clear explanation of what worked, what failed, and why.

---

## Final report

- Overleaf template: https://www.overleaf.com/read/jzfdccmknccp#17a7ee

The final report should be a synthesis of the whole project, with most emphasis on the final multi-view system and comparison with COLMAP.

**Length:** maximum **6 pages**, excluding references and appendices.

You may include your interim reports, experiment logs, extra tables, and extra figures as appendices. The main 6-page report must still be self-contained: appendices should support the main arguments. Please include a brief note on group dynamics during the last two weeks as an appendix.

Suggested structure:

1. **Project synthesis and end-to-end method**
   Approx. **1.5 pages**
   Describe the SfM problem, why it is important, and the end-to-end solution you implemented across the project. This should include SIFT features, descriptor matching, geometric verification, two-view reconstruction, triangulation, PnP registration, and visual/evaluation outputs.

2. **Week 4 extension: from 3 images to larger image sets**
   Approx. **1 page**
   Describe the final-week task, how you extended the Week 3 system, how images were added or rejected, and any design choices you made.

3. **Analysis of your final system**
   Approx. **1.5 pages**
   Analyse your final system quantitatively and qualitatively. Include evidence such as registered images, rejected images, 2D-3D correspondences, PnP inliers, reprojection errors, camera-pose visualisations, sparse point visualisations, and failure cases.

4. **Comparison with COLMAP**
   Approx. **1 page**
   Run COLMAP on the same images as your own reconstruction attempts and compare both quantitatively and qualitatively. Consider registered cameras, sparse points, camera trajectory, point-cloud density, visual plausibility, and robustness.

5. **Commentary and first-principles reflection**
   Approx. **1 page**
   Discuss what is missing from your pipeline to reach COLMAP-like quality. Connect this to your Week 1 analysis of COLMAP failure cases: from first principles, what would a more robust SfM system need in order to address those failures?

The final report should explain the whole project story and make a clear argument about what you built, what evidence you obtained, and what you learned.

---

## Presentation

Each group will give a **5-minute presentation**.

The presentation should cover the main points from the final report and tell the visual story of your project. Focus on your final multi-view reconstruction, comparison with COLMAP, and what you learned. Use figures, visualisations, and concise quantitative evidence rather than long text.

You do not need to cover every detail of the method. Prioritise the evidence and interpretation that best explain your final system.

Minimum expectations:

- description of your final method,
- show your final reconstruction,
- show the COLMAP comparison,
- include one key quantitative table or metric,
- explain one important success or failure,
- state what is missing from your pipeline to reach COLMAP-like quality, and what it might take to also fix the limitations of COLMAP.

A 5-minute presentation requires more careful preparation than a longer one. Your group should decide the key message, choose the visual results that best support it, decide who speaks for each part, and rehearse the transitions. You will not have time to show everything, so focus on the strongest evidence and clearest insights.

---

## Final deliverables

By the deadline, submit:

- final group code,
- final individual report.

Please make two uploads on moodle, one for the code and another for the report. Everyone needs to upload the report, and any one person can make the upload for the code. 

All group members should understand the submitted code, results, and presentation material.
