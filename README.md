# Booster Assets

This repository contains Booster robot models, motion data, and a simple helper package `booster_assets` for local development and tooling.

Robot Configurations
--------------------

### K1 Robot Models

| Configuration                 | Description                                         | Available Formats    |
|------------------------------|-----------------------------------------------------|----------------------|
| K1 (22 DoF)                  | 22-DoF layout: head 2 joints, arms 4 joints ×2, legs 6 joints ×2 | URDF (`robots/K1/K1_22dof.urdf`), XML (`robots/K1/K1_22dof.xml`) |
| K1 Locomotion                | Locomotion variant (fixed heads and arms)          | URDF (`robots/K1/K1_locomotion.urdf`) |
| K1 with ZED (22 DoF)         | 22-DoF variant integrated with ZED camera mounts   | URDF (`robots/K1/K1_22dof-ZED.urdf`) |

### T1 Robot Models

| Configuration                 | Description                                         | Available Formats    |
|------------------------------|-----------------------------------------------------|----------------------|
| T1 (23 DoF)           | 23-DoF layout: head 2 joints, arms 4 joints ×2, waist 1 joint, legs 6 joints ×2 | URDF (`robots/T1/T1_23dof.urdf`), XML (`robots/T1/T1_23dof.xml`) |
| T1 Locomotion (23 DoF)       | 23-DoF locomotion variant (fixed head, arms, waist where applicable)    | URDF (`robots/T1/T1_locomotion.urdf`), XML (`robots/T1/T1_locomotion.xml`) |
| T1 with 7-DoF Arms (29 DoF)       | 29-DoF layout: arm joints become 7 per arm (head 2, arms 7×2, waist 1, legs 6×2) | URDF (`robots/T1/T1_29dof.urdf`) |

Motion and Data Files
---------------------

- `motions/` contains retargeted motion data for booster robots. Currently only a few K1 example motions are provided.

### Motion CSV Format

- Each row represents one frame of a trajectory.
- The first 7 columns are the generalized base pose: base position `x, y, z` and base orientation quaternion `x, y, z, w`.
- The remaining columns are joint positions (radians).

- K1 joint order (`booster_assets.motions.K1_JOINT_NAMES`):

```text
AAHead_yaw,
Head_pitch,
ALeft_Shoulder_Pitch,
Left_Shoulder_Roll,
Left_Elbow_Pitch,
Left_Elbow_Yaw,
ARight_Shoulder_Pitch,
Right_Shoulder_Roll,
Right_Elbow_Pitch,
Right_Elbow_Yaw,
Left_Hip_Pitch,
Left_Hip_Roll,
Left_Hip_Yaw,
Left_Knee_Pitch,
Left_Ankle_Pitch,
Left_Ankle_Roll,
Right_Hip_Pitch,
Right_Hip_Roll,
Right_Hip_Yaw,
Right_Knee_Pitch,
Right_Ankle_Pitch,
Right_Ankle_Roll
```

- T1 joint order (`booster_assets.motions.T1_JOINT_NAMES`):

```text
AAHead_yaw,
Head_pitch,
Left_Shoulder_Pitch,
Left_Shoulder_Roll,
Left_Elbow_Pitch,
Left_Elbow_Yaw,
Right_Shoulder_Pitch,
Right_Shoulder_Roll,
Right_Elbow_Pitch,
Right_Elbow_Yaw,
Waist,
Left_Hip_Pitch,
Left_Hip_Roll,
Left_Hip_Yaw,
Left_Knee_Pitch,
Left_Ankle_Pitch,
Left_Ankle_Roll,
Right_Hip_Pitch,
Right_Hip_Roll,
Right_Hip_Yaw,
Right_Knee_Pitch,
Right_Ankle_Pitch,
Right_Ankle_Roll
```

### Motion List

| File Name                  | Fps | Description                                        |
|----------------------------|-----|----------------------------------------------------|
| k1_fight_001.csv           | 30  | Fighting motion sequence                           |
| k1_mj2_seg1.csv            | 50  | MJ dance segment                                   |


Python installation and usage
-----------------------------

Install the package in editable (development) mode:

```bash
python3 -m pip install -e .
```