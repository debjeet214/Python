## SHUTIL MODULE:
Shutil is a Python module that provides a higher level interface for working with file and directories. The name "shutil" is short for shell utility. It provides a convenient and efficient way to automate tasks that are commonly performed on files and directories.

The following are some of the most commonly used functions in the shutil module:

### 1. shutil.copy(src, dst)
Description: Copies the file from src to dst. The destination can be a directory or a full file path.
```python
shutil.copy('source.txt', 'destination.txt')
```

### 2. shutil.copy2(src, dst)
Description: Similar to copy(), but also attempts to preserve file metadata (e.g., timestamps).
```python
shutil.copy2('source.txt', 'destination.txt')
```

### 3. shutil.copyfile(src, dst)
Description: Copies the contents of the file named src to the file named dst.
```python
shutil.copyfile('source.txt', 'destination.txt')
```

### 4. shutil.copytree(src, dst, dirs_exist_ok=False)
Description: Recursively copies an entire directory tree rooted at src to a directory named dst.
```python
shutil.copytree('source_folder', 'destination_folder')
```

### 5. shutil.move(src, dst)
Description: Recursively moves a file or directory (src) to another location (dst). If the destination is a directory, the source is moved inside it.
```python
shutil.move('source.txt', 'destination_folder/')
```

### 6. shutil.rmtree(path)
Description: Recursively deletes a directory tree.
```python
shutil.rmtree('folder_to_delete')
```

### 7. shutil.disk_usage(path)
Description: Returns a named tuple with the total, used, and free space on the disk in bytes for the given path.
```python
usage = shutil.disk_usage('/')
print(usage)
```

8. shutil.which(cmd)
Description: Returns the path of the executable command cmd, if it exists in the system’s PATH. Returns None if not found.
```python
shutil.which('python')
```

### 9. shutil.make_archive(base_name, format[, root_dir[, base_dir[, verbose[, dry_run[, owner[, group[, logger]]]]]]])
Description: Creates an archive file (e.g., .zip, .tar) from a directory tree.
```python
shutil.make_archive('backup', 'zip', 'folder_to_archive')
```

11. shutil.unpack_archive(filename[, extract_dir[, format]])
Description: Unpacks an archive file into a directory.
```python
shutil.unpack_archive('backup.zip', 'extracted_folder')
```
