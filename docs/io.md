<!-- markdownlint-disable -->

<a href="../trajectopy_core/io/__init__.py"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

# <kbd>module</kbd> `io`
The io module provides the Python interfaces to stream handling. The builtin open function is defined in this module. 

At the top of the I/O hierarchy is the abstract base class IOBase. It defines the basic interface to a stream. Note, however, that there is no separation between reading and writing to streams; implementations are allowed to raise an OSError if they do not support a given operation. 

Extending IOBase is RawIOBase which deals simply with the reading and writing of raw bytes to a stream. FileIO subclasses RawIOBase to provide an interface to OS files. 

BufferedIOBase deals with buffering on a raw byte stream (RawIOBase). Its subclasses, BufferedWriter, BufferedReader, and BufferedRWPair buffer streams that are readable, writable, and both respectively. BufferedRandom provides a buffered interface to random access streams. BytesIO is a simple stream of in-memory bytes. 

Another IOBase subclass, TextIOBase, deals with the encoding and decoding of streams into text. TextIOWrapper, which extends it, is a buffered text interface to a buffered raw stream (`BufferedIOBase`). Finally, StringIO is an in-memory stream for text. 

Argument names are not part of the specification, and only the arguments of open() are intended to be used as keyword arguments. 

data: 

DEFAULT_BUFFER_SIZE 

 An int containing the default buffer size used by the module's buffered  I/O classes. open() uses the file's blksize (as obtained by os.stat) if  possible. 

**Global Variables**
---------------
- **DEFAULT_BUFFER_SIZE**
- **SEEK_SET**
- **SEEK_CUR**
- **SEEK_END**


---

<a href="../trajectopy_core/io/__init__.py"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `BufferedIOBase`
Base class for buffered IO objects. 

The main difference with RawIOBase is that the read() method supports omitting the size argument, and does not have a default implementation that defers to readinto(). 

In addition, read(), readinto() and write() may raise BlockingIOError if the underlying raw stream is in non-blocking mode and not ready; unlike their raw counterparts, they will never return None. 

A typical implementation should not inherit from a RawIOBase implementation, but wrap one. 





---

<a href="../trajectopy_core/io/__init__.py"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `IOBase`
The abstract base class for all I/O classes. 

This class provides dummy implementations for many methods that derived classes can override selectively; the default implementations represent a file that cannot be read, written or seeked. 

Even though IOBase does not declare read, readinto, or write because their signatures will vary, implementations and clients should consider those methods part of the interface. Also, implementations may raise UnsupportedOperation when operations they do not support are called. 

The basic type used for binary data read from or written to a file is bytes. Other bytes-like objects are accepted as method arguments too. In some cases (such as readinto), a writable object is required. Text I/O classes work with str data. 

Note that calling any method (except additional calls to close(), which are ignored) on a closed stream should raise a ValueError. 

IOBase (and its subclasses) support the iterator protocol, meaning that an IOBase object can be iterated over yielding the lines in a stream. 

IOBase also supports the :keyword:`with` statement. In this example, fp is closed after the suite of the with statement is complete: 

with open('spam.txt', 'r') as fp:  fp.write('Spam and eggs!') 





---

<a href="../trajectopy_core/io/__init__.py"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `RawIOBase`
Base class for raw binary I/O. 





---

<a href="../trajectopy_core/io/__init__.py"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `TextIOBase`
Base class for text I/O. 

This class provides a character and line based interface to stream I/O. There is no readinto method because Python's character strings are immutable. 





---

<a href="../trajectopy_core/io/__init__.py"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `UnsupportedOperation`










---

_This file was automatically generated via [lazydocs](https://github.com/ml-tooling/lazydocs)._
