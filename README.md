# Source Bone Rename
A Blender (2.80+) addon that enables you to quickly rename bones from Source games ValveBiped format to Blender styled L/R naming scheme back and forth!

# WHAT DOES IT DO?
You're setting up for a **Source** game, so you named half your armatures and you want to now mirror them. Uh-oh, **Blender** doesn't like L/R directions NOT being at the end.

Given you have a bone named like **ValveBiped.Bip01_L_UpperArm**, using **Source to Blender**, your bone will now be named **ValveBiped.Bip01_UpperArm.L**, and this will be done for every bone! The tool also has the option to revert from **Blender** naming scheme back to **Source** naming scheme using **Blender to Source** instead.

Look into **TODO** part to see what's upcoming.

# INSTALLATION
1. Download the [latest version from the Releases](https://github.com/ASertacAkkaya/source-bone-rename/releases/latest).
2. Load up Blender 2.80+, navigate to **Edit > Preferences...**.
3. From **Addons** tab, click the **Install...** button, select the downloaded **.zip** file, confirm selection.
4. Click the check box next to the addon to activate it.

# USAGE
- In **Object Mode**, you can find it under it's own tab, by toggling panels by **N**. Using this functionality in **Object Mode** will do the rename for every bone under multiple armatures at the same time.
- In **(Armature) Edit Mode**, you can again access it under it's own tab, same place as the **Object Mode**. In addition, you will also find the options under the **Armature > Names**, as well as when right clicking a bone, under the **Names** menu. Using this functionality in **Edit Mode** will do the rename for every bone under currently selected/edited armature.

# TODO
- Mirror ValveBiped or MMD bones
- Convert between MMD bones and ValveBiped bones
- Convert between generic bone names and ValveBiped bones
- Blender 2.77+ support
