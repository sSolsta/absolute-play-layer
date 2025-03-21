# me when i translate perl to python

import os
import traceback
import xml.etree.ElementTree as ET

def canonicalise_link(link):
    directory = os.path.dirname(path)
    if link.startswith("$(MSBuildProgramFiles32)"):
        return ""  # dont bother and hope it still works
    if link.startswith("$(ProjectDir)"):
        link = os.path.join(directory, link.replace("$(ProjectDir)", ""))
        return os.path.relpath(link)
    elif link.startswith("$"):
        print(link)
        panic(fuck)
    else:
        link = os.path.join(directory, link)
        return os.path.relpath(link)

try:
    path = r"E:\cocos2d-x-2.2.3\cocos2dx\proj.win32\cocos2d.vcxproj"
    target_conf = "Release|Win32"
    
    # python is annoying with namespaces
    ns = {"": "http://schemas.microsoft.com/developer/msbuild/2003"}
    
    main_tree = ET.parse(path)
    main_root = main_tree.getroot()
    filters_tree = ET.parse(path+".filters")
    filters_root = filters_tree.getroot()
    
    target = main_root.find("PropertyGroup[@Label='Globals']", ns).find("ProjectName", ns).text
    
    for prop_group in main_root.findall("PropertyGroup[@Label='Configuration']", ns):
        if target_conf in prop_group.get("Condition"):
            target_prop = prop_group
            break
    
    target_cond = target_prop.get("Condition")
    
    srcs = []
    headers = []
    
    for item_group in main_root.findall("ItemGroup", ns):
        if item_group.get("Label") == "ProjectConfigurations":
            continue
        for child in item_group:
            if child.find("ExcludedFromBuild"):
                fuck(this)
            if child.tag.endswith("ClCompile"):
                srcs.append(canonicalise_link(child.get("Include")))
            else:
                headers.append(canonicalise_link(child.get("Include")))
    
    item_def_ref = main_root.find(f'ItemDefinitionGroup[@Condition="{target_cond}"]', ns)
    
    filters = {}
    
    filter_groups = filters_root.findall("ItemGroup", ns)
    for filter in filter_groups[0]:
        filters[filter.get("Include")] = []
    
    for file in filter_groups[1]:
        filter = file.find("Filter", ns)
        if filter is not None:
            filters[filter.text].append(file.get("Include"))
    
    for file in filter_groups[2]:
        filter = file.find("Filter", ns)
        if filter is not None:
            filters[filter.text].append(file.get("Include"))
    
    includes = item_def_ref.find("ClCompile", ns).find("AdditionalIncludeDirectories", ns).text
    includes = includes.replace("%(AdditionalIncludeDirectories)", "").split(";")
    includes = [canonicalise_link(i) for i in includes]
    
    defs = item_def_ref.find("ClCompile", ns).find("PreprocessorDefinitions", ns).text
    defs = defs.replace("%(PreprocessorDefinitions)", "").split(";")
    
    deps = item_def_ref.find("Link", ns).find("AdditionalDependencies", ns).text
    deps = deps.replace("%(AdditionalDependencies)", "").split(";")
    
    
    type = target_prop.find("ConfigurationType", ns).text
    charset = target_prop.find("CharacterSet", ns).text
    
    with open(path + ".txt", "w") as f:
        if charset == "Unicode":
            f.write("add_definitions(-DUNICODE -D_UNICODE)\n\n")
        
        if type == "DynamicLibrary":
            f.write(f"add_library({target} SHARED")
        else:
            print(type)
            panic(fuck)
        
        for src in srcs:
            f.write("\n    ")
            f.write(src.replace("\\", "/"))
        
        f.write("\n)\n\n")
        
        f.write(f"target_include_directories({target} PUBLIC")
        for inc in includes:
            f.write("\n    ")
            f.write(inc.replace("\\", "/"))
        
        f.write("\n)\n\n")
        
        
        f.write(f"target_link_libraries({target}")
        for dep in deps:
            f.write("\n    ")
            f.write(dep.replace("\\", "/"))
        
        f.write("\n)\n\n")
    
    print(*defs)
    
    
    
except Exception:
    traceback.print_exc()

input("\nnow you can fuck off\n")