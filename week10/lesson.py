x=2**64
y=2**64
print(x==y,x is y)

x=2**128
y=2**128
print(x==y,x is y)

S1="""
<!DOCTYPE html>

<html lang="zh_CN">
  <head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" /><meta name="generator" content="Docutils 0.17.1: http://docutils.sourceforge.net/" />

    <title>zlib --- 与 gzip 兼容的压缩 &#8212; Python 3.10.8 文档</title><meta name="viewport" content="width=device-width, initial-scale=1.0">
    
    <link rel="stylesheet" href="../_static/pygments.css" type="text/css" />
    <link rel="stylesheet" href="../_static/pydoctheme.css?2022.1" type="text/css" />
    
    <script id="documentation_options" data-url_root="../" src="../_static/documentation_options.js"></script>
    <script src="../_static/jquery.js"></script>
    <script src="../_static/underscore.js"></script>
    <script src="../_static/doctools.js"></script>
    <script src="../_static/translations.js"></script>
    
    <script src="../_static/sidebar.js"></script>
    
    <link rel="search" type="application/opensearchdescription+xml"
          title="在 Python 3.10.8 文档 中搜索"
          href="../_static/opensearch.xml"/>
    <link rel="author" title="关于这些文档" href="../about.html" />
    <link rel="index" title="索引" href="../genindex.html" />
    <link rel="search" title="搜索" href="../search.html" />
    <link rel="copyright" title="版权所有" href="../copyright.html" />
    <link rel="next" title="gzip --- 对 gzip 格式的支持" href="gzip.html" />
    <link rel="prev" title="数据压缩和存档" href="archiving.html" />
    <link rel="canonical" href="https://docs.python.org/3/library/zlib.html" />
    
      
    

    
    <style>
      @media only screen {
        table.full-width-table {
            width: 100%;
        }
      }
    </style>
<link rel="shortcut icon" type="image/png" href="../_static/py.svg" />
            <script type="text/javascript" src="../_static/copybutton.js"></script>
            <script type="text/javascript" src="../_static/menu.js"></script> 

  </head>
<body>
<div class="mobile-nav">
    <input type="checkbox" id="menuToggler" class="toggler__input" aria-controls="navigation"
           aria-pressed="false" aria-expanded="false" role="button" aria-label="Menu" />
    <label for="menuToggler" class="toggler__label">
        <span></span>
    </label>
    <nav class="nav-content" role="navigation">
         <a href="https://www.python.org/" class="nav-logo">
             <img src="../_static/py.svg" alt="Logo"/>
         </a>
        <div class="version_switcher_placeholder"></div>
        <form role="search" class="search" action="../search.html" method="get">
            <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" class="search-icon">
                <path fill-rule="nonzero"
                        d="M15.5 14h-.79l-.28-.27a6.5 6.5 0 001.48-5.34c-.47-2.78-2.79-5-5.59-5.34a6.505 6.505 0 00-7.27 7.27c.34 2.8 2.56 5.12 5.34 5.59a6.5 6.5 0 005.34-1.48l.27.28v.79l4.25 4.25c.41.41 1.08.41 1.49 0 .41-.41.41-1.08 0-1.49L15.5 14zm-6 0C7.01 14 5 11.99 5 9.5S7.01 5 9.5 5 14 7.01 14 9.5 11.99 14 9.5 14z" fill="#444"></path>
            </svg>
            <input type="text" name="q" aria-label="快速搜索"/>
            <input type="submit" value="转向"/>
        </form>
    </nav>
    <div class="menu-wrapper">
        <nav class="menu" role="navigation" aria-label="main navigation">
            <div class="language_switcher_placeholder"></div>
  <h4>上一个主题</h4>
  <p class="topless"><a href="archiving.html"
                        title="上一章">数据压缩和存档</a></p>
  <h4>下一个主题</h4>
  <p class="topless"><a href="gzip.html"
                        title="下一章"><code class="xref py py-mod docutils literal notranslate"><span class="pre">gzip</span></code> --- 对 <strong class="program">gzip</strong> 格式的支持</a></p>
  <div role="note" aria-label="source link">
    <h3>当前页面</h3>
    <ul class="this-page-menu">
      <li><a href="../bugs.html">提交 Bug</a></li>
      <li>
        <a href="https://github.com/python/cpython/blob/3.10/Doc/library/zlib.rst"
            rel="nofollow">显示源码
        </a>
      </li>
    </ul>
  </div>
        </nav>
    </div>
</div>

  
    <div class="related" role="navigation" aria-label="related navigation">
      <h3>导航</h3>
      <ul>
        <li class="right" style="margin-right: 10px">
          <a href="../genindex.html" title="总目录"
             accesskey="I">索引</a></li>
        <li class="right" >
          <a href="../py-modindex.html" title="Python 模块索引"
             >模块</a> |</li>
        <li class="right" >
          <a href="gzip.html" title="gzip --- 对 gzip 格式的支持"
             accesskey="N">下一页</a> |</li>
        <li class="right" >
          <a href="archiving.html" title="数据压缩和存档"
             accesskey="P">上一页</a> |</li>

          <li><img src="../_static/py.svg" alt="python logo" style="vertical-align: middle; margin-top: -1px"/></li>
          <li><a href="https://www.python.org/">Python</a> &#187;</li>
          <li class="switchers">
            <div class="language_switcher_placeholder"></div>
            <div class="version_switcher_placeholder"></div>
          </li>
          <li>
              
          </li>
    <li id="cpython-language-and-version">
      <a href="../index.html">3.10.8 Documentation</a> &#187;
    </li>

          <li class="nav-item nav-item-1"><a href="index.html" >Python 标准库</a> &#187;</li>
          <li class="nav-item nav-item-2"><a href="archiving.html" accesskey="U">数据压缩和存档</a> &#187;</li>
        <li class="nav-item nav-item-this"><a href=""><code class="xref py py-mod docutils literal notranslate"><span class="pre">zlib</span></code> --- 与 <strong class="program">gzip</strong> 兼容的压缩</a></li>
                <li class="right">
                    

    <div class="inline-search" role="search">
        <form class="inline-search" action="../search.html" method="get">
          <input placeholder="快速搜索" aria-label="快速搜索" type="text" name="q" />
          <input type="submit" value="转向" />
          <input type="hidden" name="check_keywords" value="yes" />
          <input type="hidden" name="area" value="default" />
        </form>
    </div>
                     |
                </li>
            
      </ul>
    </div>    

    <div class="document">
      <div class="documentwrapper">
        <div class="bodywrapper">
          <div class="body" role="main">
            
  <section id="module-zlib">
<span id="zlib-compression-compatible-with-gzip"></span><h1><a class="reference internal" href="#module-zlib" title="zlib: Low-level interface to compression and decompression routines compatible with gzip."><code class="xref py py-mod docutils literal notranslate"><span class="pre">zlib</span></code></a> --- 与 <strong class="program">gzip</strong> 兼容的压缩<a class="headerlink" href="#module-zlib" title="永久链接至标题">¶</a></h1>
<hr class="docutils" />
<p>对于需要数据压缩的应用，此模块中的函数允许使用 zlib 库进行压缩和解压缩。 zlib 库的项目主页是 <a class="reference external" href="https://www.zlib.net">https://www.zlib.net</a>。 已知此 Python 模块与 1.1.3 之前版本的 zlib 库存在不兼容；1.1.3 版则存在一个 <a class="reference external" href="https://zlib.net/zlib_faq.html#faq33">安全缺陷</a>，因此我们推荐使用 1.1.4 或更新的版本。</p>
<p>zlib 的函数有很多选项，一般需要按特定顺序使用。本文档没有覆盖全部的用法。更多详细信息请于 <a class="reference external" href="http://www.zlib.net/manual.html">http://www.zlib.net/manual.html</a> 参阅官方手册。</p>
<p>要读写 <code class="docutils literal notranslate"><span class="pre">.gz</span></code> 格式的文件，请参考 <a class="reference internal" href="gzip.html#module-gzip" title="gzip: Interfaces for gzip compression and decompression using file objects."><code class="xref py py-mod docutils literal notranslate"><span class="pre">gzip</span></code></a> 模块。</p>
<p>此模块中可用的异常和函数如下：</p>
<dl class="py exception">
<dt id="zlib.error">
<em class="property">exception </em><code class="sig-prename descclassname">zlib.</code><code class="sig-name descname">error</code><a class="headerlink" href="#zlib.error" title="永久链接至目标">¶</a></dt>
<dd><p>在压缩或解压缩过程中发生错误时的异常。</p>
</dd></dl>

<dl class="py function">
<dt id="zlib.adler32">
<code class="sig-prename descclassname">zlib.</code><code class="sig-name descname">adler32</code><span class="sig-paren">(</span><em class="sig-param">data</em><span class="optional">[</span>, <em class="sig-param">value</em><span class="optional">]</span><span class="sig-paren">)</span><a class="headerlink" href="#zlib.adler32" title="永久链接至目标">¶</a></dt>
<dd><p>计算 <em>data</em> 的 Adler-32 校验值。(Adler-32 校验的可靠性与 CRC32 基本相当，但比计算 CRC32 更高效。) 计算的结果是一个 32 位的整数。参数 <em>value</em> 是校验时的起始值，其默认值为 1。借助参数 <em>value</em> 可为分段的输入计算校验值。此算法没有加密强度，不应用于身份验证和数字签名。此算法的目的仅为验证数据的正确性，不适合作为通用散列算法。</p>
<div class="versionchanged">
<p><span class="versionmodified changed">在 3.0 版更改: </span>结果值将始终为无符号类型。 要在使用 Python 2 或更早版本时生成同样的数值，请使用 <code class="docutils literal notranslate"><span class="pre">adler32(data)</span> <span class="pre">&amp;</span> <span class="pre">0xffffffff</span></code>。</p>
</div>
</dd></dl>

<dl class="py function">
<dt id="zlib.compress">
<code class="sig-prename descclassname">zlib.</code><code class="sig-name descname">compress</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">data</span></em>, <em class="sig-param"><span class="o">/</span></em>, <em class="sig-param"><span class="n">level</span><span class="o">=</span><span class="default_value">- 1</span></em><span class="sig-paren">)</span><a class="headerlink" href="#zlib.compress" title="永久链接至目标">¶</a></dt>
<dd><p>压缩 <em>data</em> 中的字节，返回含有已压缩内容的 bytes 对象。参数 <em>level</em> 为整数，可取值为 <code class="docutils literal notranslate"><span class="pre">0</span></code> 到 <code class="docutils literal notranslate"><span class="pre">9</span></code> 或 <code class="docutils literal notranslate"><span class="pre">-1</span></code>，用于指定压缩等级。<code class="docutils literal notranslate"><span class="pre">1</span></code> (Z_BEST_SPEED) 表示最快速度和最低压缩率，<code class="docutils literal notranslate"><span class="pre">9</span></code> (Z_BEST_COMPRESSION) 表示最慢速度和最高压缩率。<code class="docutils literal notranslate"><span class="pre">0</span></code> (Z_NO_COMPRESSION) 表示不压缩。参数默认值为 <code class="docutils literal notranslate"><span class="pre">-1</span></code> (Z_DEFAULT_COMPRESSION)。Z_DEFAULT_COMPRESSION 是速度和压缩率之间的平衡 (一般相当于设压缩等级为 6)。函数发生错误时抛出 <a class="reference internal" href="#zlib.error" title="zlib.error"><code class="xref py py-exc docutils literal notranslate"><span class="pre">error</span></code></a> 异常。</p>
<div class="versionchanged">
<p><span class="versionmodified changed">在 3.6 版更改: </span>现在，<em>level</em> 可作为关键字参数。</p>
</div>
</dd></dl>

<dl class="py function">
<dt id="zlib.compressobj">
<code class="sig-prename descclassname">zlib.</code><code class="sig-name descname">compressobj</code><span class="sig-paren">(</span><em class="sig-param">level=-1</em>, <em class="sig-param">method=DEFLATED</em>, <em class="sig-param">wbits=MAX_WBITS</em>, <em class="sig-param">memLevel=DEF_MEM_LEVEL</em>, <em class="sig-param">strategy=Z_DEFAULT_STRATEGY</em><span class="optional">[</span>, <em class="sig-param">zdict</em><span class="optional">]</span><span class="sig-paren">)</span><a class="headerlink" href="#zlib.compressobj" title="永久链接至目标">¶</a></dt>
<dd><p>返回一个 压缩对象，用来压缩内存中难以容下的数据流。</p>
<p>参数 <em>level</em> 为压缩等级，是整数，可取值为 <code class="docutils literal notranslate"><span class="pre">0</span></code> 到 <code class="docutils literal notranslate"><span class="pre">9</span></code> 或 <code class="docutils literal notranslate"><span class="pre">-1</span></code>。<code class="docutils literal notranslate"><span class="pre">1</span></code> (Z_BEST_SPEED) 表示最快速度和最低压缩率，<code class="docutils literal notranslate"><span class="pre">9</span></code> (Z_BEST_COMPRESSION) 表示最慢速度和最高压缩率。<code class="docutils literal notranslate"><span class="pre">0</span></code> (Z_NO_COMPRESSION) 表示不压缩。参数默认值为 <code class="docutils literal notranslate"><span class="pre">-1</span></code> (Z_DEFAULT_COMPRESSION)。Z_DEFAULT_COMPRESSION 是速度和压缩率之间的平衡 (一般相当于设压缩等级为 6)。</p>
<p><em>method</em> 表示压缩算法。现在只支持 <code class="xref py py-const docutils literal notranslate"><span class="pre">DEFLATED</span></code> 这个算法。</p>
<p>参数 <em>wbits</em> 指定压缩数据时所使用的历史缓冲区的大小 (窗口大小)，并指定压缩输出是否包含头部或尾部。参数的默认值是 <code class="docutils literal notranslate"><span class="pre">15</span></code> (MAX_WBITS)。参数的值分为几个范围：</p>
<ul class="simple">
<li><p>+9 至 +15：窗口大小以二为底的对数。 即这些值对应着 512 至 32768 的窗口大小。 更大的值会提供更好的压缩，同时内存开销也会更大。 压缩输出会包含 zlib 特定格式的头部和尾部。</p></li>
<li><p>−9 至 −15：绝对值为窗口大小以二为底的对数。 压缩输出仅包含压缩数据，没有头部和尾部。</p></li>
<li><p>+25 至 +31 = 16 + (9 至 15)：后 4 个比特位为窗口大小以二为底的对数。 压缩输出包含一个基本的 <strong class="program">gzip</strong> 头部，并以校验和为尾部。</p></li>
</ul>
<p>参数 <em>memLevel</em> 指定内部压缩操作时所占用内存大小。参数取 <code class="docutils literal notranslate"><span class="pre">1</span></code> 到 <code class="docutils literal notranslate"><span class="pre">9</span></code>。更大的值占用更多的内存，同时速度也更快输出也更小。</p>
<p>参数 <em>strategy</em> 用于调节压缩算法。可取值为  <code class="xref py py-const docutils literal notranslate"><span class="pre">Z_DEFAULT_STRATEGY</span></code>、<code class="xref py py-const docutils literal notranslate"><span class="pre">Z_FILTERED</span></code>、<code class="xref py py-const docutils literal notranslate"><span class="pre">Z_HUFFMAN_ONLY</span></code>、<code class="xref py py-const docutils literal notranslate"><span class="pre">Z_RLE</span></code> (zlib 1.2.0.1) 或 <code class="xref py py-const docutils literal notranslate"><span class="pre">Z_FIXED</span></code> (zlib 1.2.2.2)。</p>
<p>参数 <em>zdict</em> 指定预定义的压缩字典。它是一个字节序列 (如 <a class="reference internal" href="stdtypes.html#bytes" title="bytes"><code class="xref py py-class docutils literal notranslate"><span class="pre">bytes</span></code></a> 对象)，其中包含用户认为要压缩的数据中可能频繁出现的子序列。频率高的子序列应当放在字典的尾部。</p>
<div class="versionchanged">
<p><span class="versionmodified changed">在 3.3 版更改: </span>添加关键字参数 <em>zdict</em>。</p>
</div>
</dd></dl>

<dl class="py function">
<dt id="zlib.crc32">
<code class="sig-prename descclassname">zlib.</code><code class="sig-name descname">crc32</code><span class="sig-paren">(</span><em class="sig-param">data</em><span class="optional">[</span>, <em class="sig-param">value</em><span class="optional">]</span><span class="sig-paren">)</span><a class="headerlink" href="#zlib.crc32" title="永久链接至目标">¶</a></dt>
<dd><p id="index-0">计算 <em>data</em> 的 CRC (循环冗余校验) 值。计算的结果是一个 32 位的整数。参数 <em>value</em> 是校验时的起始值，其默认值为 0。借助参数 <em>value</em> 可为分段的输入计算校验值。此算法没有加密强度，不应用于身份验证和数字签名。此算法的目的仅为验证数据的正确性，不适合作为通用散列算法。</p>
<div class="versionchanged">
<p><span class="versionmodified changed">在 3.0 版更改: </span>结果值将始终为无符号类型。 要在使用 Python 2 或更早版本时生成同样的数值，请使用 <code class="docutils literal notranslate"><span class="pre">crc32(data)</span> <span class="pre">&amp;</span> <span class="pre">0xffffffff</span></code>。</p>
</div>
</dd></dl>

<dl class="py function">
<dt id="zlib.decompress">
<code class="sig-prename descclassname">zlib.</code><code class="sig-name descname">decompress</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">data</span></em>, <em class="sig-param"><span class="o">/</span></em>, <em class="sig-param"><span class="n">wbits</span><span class="o">=</span><span class="default_value">MAX_WBITS</span></em>, <em class="sig-param"><span class="n">bufsize</span><span class="o">=</span><span class="default_value">DEF_BUF_SIZE</span></em><span class="sig-paren">)</span><a class="headerlink" href="#zlib.decompress" title="永久链接至目标">¶</a></dt>
<dd><p>解压 <em>data</em> 中的字节，返回含有已解压内容的 bytes 对象。参数 <em>wbits</em> 取决于 <em>data</em> 的格式，具体参见下边的说明。<em>bufsize</em> 为输出缓冲区的起始大小。函数发生错误时抛出 <a class="reference internal" href="#zlib.error" title="zlib.error"><code class="xref py py-exc docutils literal notranslate"><span class="pre">error</span></code></a> 异常。</p>
<p id="decompress-wbits"><em>wbits</em> 形参控制历史缓冲区的大小（或称“窗口大小”）以及所期望的头部和尾部格式。 它类似于 <a class="reference internal" href="#zlib.compressobj" title="zlib.compressobj"><code class="xref py py-func docutils literal notranslate"><span class="pre">compressobj()</span></code></a> 的形参，但可接受更大范围的值：</p>
<ul class="simple">
<li><p>+8 至 +15：窗口尺寸以二为底的对数。 输入必须包含 zlib 头部和尾部。</p></li>
<li><p>0：根据 zlib 头部自动确定窗口大小。 只从 zlib 1.2.3.5 版起受支持。</p></li>
<li><p>−8 至 −15：使用 <em>wbits</em> 的绝对值作为窗口大小以二为底的对数。 输入必须为原始数据流，没有头部和尾部。</p></li>
<li><p>+24 至 +31 = 16 + (8 至 15)：使用后 4 个比特位作为窗口大小以二为底的对数。 输入必须包括 gzip 头部和尾部。</p></li>
<li><p>+40 至 +47 = 32 + (8 至 15)：使用后 4 个比特位作为窗口大小以二为底的对数，并且自动接受 zlib 或 gzip 格式。</p></li>
</ul>
<p>当解压缩一个数据流时，窗口大小必须不小于用于压缩数据流的原始窗口大小；使用太小的值可能导致 <a class="reference internal" href="#zlib.error" title="zlib.error"><code class="xref py py-exc docutils literal notranslate"><span class="pre">error</span></code></a> 异常。 默认 <em>wbits</em> 值对应于最大的窗口大小并且要求包括 zlib 头部和尾部。</p>
<p><em>bufsize</em> 是用于存放解压数据的缓冲区初始大小。 如果需要更大空间，缓冲区大小将按需增加，因此你不需要让这个值完全精确；对其进行调整仅会节省一点对 <code class="xref c c-func docutils literal notranslate"><span class="pre">malloc()</span></code> 的调用次数。</p>
<div class="versionchanged">
<p><span class="versionmodified changed">在 3.6 版更改: </span><em>wbits</em> 和 <em>bufsize</em> 可用作关键字参数。</p>
</div>
</dd></dl>

<dl class="py function">
<dt id="zlib.decompressobj">
<code class="sig-prename descclassname">zlib.</code><code class="sig-name descname">decompressobj</code><span class="sig-paren">(</span><em class="sig-param">wbits=MAX_WBITS</em><span class="optional">[</span>, <em class="sig-param">zdict</em><span class="optional">]</span><span class="sig-paren">)</span><a class="headerlink" href="#zlib.decompressobj" title="永久链接至目标">¶</a></dt>
<dd><p>返回一个解压对象，用来解压无法被一次性放入内存的数据流。</p>
<p><em>wbits</em> 形参控制历史缓冲区的大小（或称“窗口大小”）以及所期望的头部和尾部格式。 它的含义与 <a class="reference external" href="#decompress-wbits">对 decompress() 的描述</a> 相同。</p>
<p><em>zdict</em> 形参指定指定一个预定义的压缩字典。 如果提供了此形参，它必须与产生将解压数据的压缩器所使用的字典相同。</p>
<div class="admonition note">
<p class="admonition-title">注解</p>
<p>如果 <em>zdict</em> 是一个可变对象 (例如 <a class="reference internal" href="stdtypes.html#bytearray" title="bytearray"><code class="xref py py-class docutils literal notranslate"><span class="pre">bytearray</span></code></a>)，则你不可在对 <a class="reference internal" href="#zlib.decompressobj" title="zlib.decompressobj"><code class="xref py py-func docutils literal notranslate"><span class="pre">decompressobj()</span></code></a> 的调用和对解压器的 <code class="docutils literal notranslate"><span class="pre">decompress()</span></code> 方法的调用之间修改其内容。</p>
</div>
<div class="versionchanged">
<p><span class="versionmodified changed">在 3.3 版更改: </span>增加了 <em>zdict</em> 形参。</p>
</div>
</dd></dl>

<p>压缩对象支持以下方法：</p>
<dl class="py method">
<dt id="zlib.Compress.compress">
<code class="sig-prename descclassname">Compress.</code><code class="sig-name descname">compress</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">data</span></em><span class="sig-paren">)</span><a class="headerlink" href="#zlib.Compress.compress" title="永久链接至目标">¶</a></dt>
<dd><p>压缩 <em>data</em> 并返回 bytes 对象，这个对象含有 <em>data</em> 的部分或全部内容的已压缩数据。所得的对象必须拼接在上一次调用 <a class="reference internal" href="#zlib.compress" title="zlib.compress"><code class="xref py py-meth docutils literal notranslate"><span class="pre">compress()</span></code></a> 方法所得数据的后面。缓冲区中可能留存部分输入以供下一次调用。</p>
</dd></dl>

<dl class="py method">
<dt id="zlib.Compress.flush">
<code class="sig-prename descclassname">Compress.</code><code class="sig-name descname">flush</code><span class="sig-paren">(</span><span class="optional">[</span><em class="sig-param">mode</em><span class="optional">]</span><span class="sig-paren">)</span><a class="headerlink" href="#zlib.Compress.flush" title="永久链接至目标">¶</a></dt>
<dd><p>压缩所有缓冲区的数据并返回已压缩的数据。参数 <em>mode</em> 可以传入的常量为：<code class="xref py py-const docutils literal notranslate"><span class="pre">Z_NO_FLUSH</span></code>、<code class="xref py py-const docutils literal notranslate"><span class="pre">Z_PARTIAL_FLUSH</span></code>、<code class="xref py py-const docutils literal notranslate"><span class="pre">Z_SYNC_FLUSH</span></code>、<code class="xref py py-const docutils literal notranslate"><span class="pre">Z_FULL_FLUSH</span></code>、<code class="xref py py-const docutils literal notranslate"><span class="pre">Z_BLOCK</span></code> (zlib 1.2.3.4) 或 <code class="xref py py-const docutils literal notranslate"><span class="pre">Z_FINISH</span></code>。默认值为 <code class="xref py py-const docutils literal notranslate"><span class="pre">Z_FINISH</span></code>。<code class="xref py py-const docutils literal notranslate"><span class="pre">Z_FINISH</span></code> 关闭已压缩数据流并不允许再压缩其他数据，<code class="xref py py-const docutils literal notranslate"><span class="pre">Z_FINISH</span></code>  以外的值皆允许这个对象继续压缩数据。调用 <a class="reference internal" href="#zlib.Compress.flush" title="zlib.Compress.flush"><code class="xref py py-meth docutils literal notranslate"><span class="pre">flush()</span></code></a> 方法并将 <em>mode</em> 设为 <code class="xref py py-const docutils literal notranslate"><span class="pre">Z_FINISH</span></code> 后会无法再次调用 <a class="reference internal" href="#zlib.compress" title="zlib.compress"><code class="xref py py-meth docutils literal notranslate"><span class="pre">compress()</span></code></a>，此时只能删除这个对象。</p>
</dd></dl>

<dl class="py method">
<dt id="zlib.Compress.copy">
<code class="sig-prename descclassname">Compress.</code><code class="sig-name descname">copy</code><span class="sig-paren">(</span><span class="sig-paren">)</span><a class="headerlink" href="#zlib.Compress.copy" title="永久链接至目标">¶</a></dt>
<dd><p>返回此压缩对象的一个拷贝。它可以用来高效压缩一系列拥有相同前缀的数据。</p>
</dd></dl>

<div class="versionchanged">
<p><span class="versionmodified changed">在 3.8 版更改: </span>添加了对压缩对象执行 <a class="reference internal" href="copy.html#copy.copy" title="copy.copy"><code class="xref py py-func docutils literal notranslate"><span class="pre">copy.copy()</span></code></a> 和 <a class="reference internal" href="copy.html#copy.deepcopy" title="copy.deepcopy"><code class="xref py py-func docutils literal notranslate"><span class="pre">copy.deepcopy()</span></code></a> 的支持。</p>
</div>
<p>解压缩对象支持以下方法：</p>
<dl class="py attribute">
<dt id="zlib.Decompress.unused_data">
<code class="sig-prename descclassname">Decompress.</code><code class="sig-name descname">unused_data</code><a class="headerlink" href="#zlib.Decompress.unused_data" title="永久链接至目标">¶</a></dt>
<dd><p>一个 bytes 对象，其中包含压缩数据结束之后的任何字节数据。 也就是说，它将为 <code class="docutils literal notranslate"><span class="pre">b&quot;&quot;</span></code> 直到包含压缩数据的末尾字节可用。 如果整个结果字节串都包含压缩数据，它将为一个空的 bytes 对象 <code class="docutils literal notranslate"><span class="pre">b&quot;&quot;</span></code>。</p>
</dd></dl>

<dl class="py attribute">
<dt id="zlib.Decompress.unconsumed_tail">
<code class="sig-prename descclassname">Decompress.</code><code class="sig-name descname">unconsumed_tail</code><a class="headerlink" href="#zlib.Decompress.unconsumed_tail" title="永久链接至目标">¶</a></dt>
<dd><p>一个 bytes 对象，其中包含未被上一次 <a class="reference internal" href="#zlib.decompress" title="zlib.decompress"><code class="xref py py-meth docutils literal notranslate"><span class="pre">decompress()</span></code></a> 调用所消耗的任何数据。 此数据不能被 zlib 机制看到，因此你必须将其送回（可能要附带额外的数据拼接）到后续的 <a class="reference internal" href="#zlib.decompress" title="zlib.decompress"><code class="xref py py-meth docutils literal notranslate"><span class="pre">decompress()</span></code></a> 方法调用以获得正确的输出。</p>
</dd></dl>

<dl class="py attribute">
<dt id="zlib.Decompress.eof">
<code class="sig-prename descclassname">Decompress.</code><code class="sig-name descname">eof</code><a class="headerlink" href="#zlib.Decompress.eof" title="永久链接至目标">¶</a></dt>
<dd><p>一个布尔值，指明是否已到达压缩数据流的末尾。</p>
<p>This makes it possible to distinguish between a properly formed compressed
stream, and an incomplete or truncated one.</p>
<div class="versionadded">
<p><span class="versionmodified added">3.3 新版功能.</span></p>
</div>
</dd></dl>

<dl class="py method">
<dt id="zlib.Decompress.decompress">
<code class="sig-prename descclassname">Decompress.</code><code class="sig-name descname">decompress</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">data</span></em>, <em class="sig-param"><span class="n">max_length</span><span class="o">=</span><span class="default_value">0</span></em><span class="sig-paren">)</span><a class="headerlink" href="#zlib.Decompress.decompress" title="永久链接至目标">¶</a></dt>
<dd><p>解压缩 <em>data</em> 并返回 bytes 对象，其中包含对应于 <em>string</em> 中至少一部分数据的解压缩数据。 此数据应当被拼接到之前任何对 <a class="reference internal" href="#zlib.decompress" title="zlib.decompress"><code class="xref py py-meth docutils literal notranslate"><span class="pre">decompress()</span></code></a> 方法的调用所产生的输出。 部分输入数据可能会被保留在内部缓冲区以供后续处理。</p>
<p>如果可选的形参 <em>max_length</em> 非零则返回值将不会长于 <em>max_length</em>。 这可能意味着不是所有已压缩输入都能被处理；并且未被消耗的数据将被保存在 <a class="reference internal" href="#zlib.Decompress.unconsumed_tail" title="zlib.Decompress.unconsumed_tail"><code class="xref py py-attr docutils literal notranslate"><span class="pre">unconsumed_tail</span></code></a> 属性中。 如果要继续解压缩则这个字节串必须被传给对 <a class="reference internal" href="#zlib.decompress" title="zlib.decompress"><code class="xref py py-meth docutils literal notranslate"><span class="pre">decompress()</span></code></a> 的后续调用。 如果 <em>max_length</em> 为零则整个输入都会被解压缩，并且 <a class="reference internal" href="#zlib.Decompress.unconsumed_tail" title="zlib.Decompress.unconsumed_tail"><code class="xref py py-attr docutils literal notranslate"><span class="pre">unconsumed_tail</span></code></a> 将为空。</p>
<div class="versionchanged">
<p><span class="versionmodified changed">在 3.6 版更改: </span><em>max_length</em> 可用作关键字参数。</p>
</div>
</dd></dl>

<dl class="py method">
<dt id="zlib.Decompress.flush">
<code class="sig-prename descclassname">Decompress.</code><code class="sig-name descname">flush</code><span class="sig-paren">(</span><span class="optional">[</span><em class="sig-param">length</em><span class="optional">]</span><span class="sig-paren">)</span><a class="headerlink" href="#zlib.Decompress.flush" title="永久链接至目标">¶</a></dt>
<dd><p>所有挂起的输入会被处理，并且返回包含剩余未压缩输出的 bytes 对象。 在调用 <a class="reference internal" href="#zlib.Decompress.flush" title="zlib.Decompress.flush"><code class="xref py py-meth docutils literal notranslate"><span class="pre">flush()</span></code></a> 之后，<a class="reference internal" href="#zlib.decompress" title="zlib.decompress"><code class="xref py py-meth docutils literal notranslate"><span class="pre">decompress()</span></code></a> 方法将无法被再次调用；唯一可行的操作是删除该对象。</p>
<p>可选的形参 <em>length</em> 设置输出缓冲区的初始大小。</p>
</dd></dl>

<dl class="py method">
<dt id="zlib.Decompress.copy">
<code class="sig-prename descclassname">Decompress.</code><code class="sig-name descname">copy</code><span class="sig-paren">(</span><span class="sig-paren">)</span><a class="headerlink" href="#zlib.Decompress.copy" title="永久链接至目标">¶</a></dt>
<dd><p>返回解压缩对象的一个拷贝。 它可以用来在数据流的中途保存解压缩器的状态以便加快随机查找数据流后续位置的速度。</p>
</dd></dl>

<div class="versionchanged">
<p><span class="versionmodified changed">在 3.8 版更改: </span>添加了对解压缩对象执行 <a class="reference internal" href="copy.html#copy.copy" title="copy.copy"><code class="xref py py-func docutils literal notranslate"><span class="pre">copy.copy()</span></code></a> 和 <a class="reference internal" href="copy.html#copy.deepcopy" title="copy.deepcopy"><code class="xref py py-func docutils literal notranslate"><span class="pre">copy.deepcopy()</span></code></a> 的支持。</p>
</div>
<p>通过下列常量可获取模块所使用的 zlib 库的版本信息：</p>
<dl class="py data">
<dt id="zlib.ZLIB_VERSION">
<code class="sig-prename descclassname">zlib.</code><code class="sig-name descname">ZLIB_VERSION</code><a class="headerlink" href="#zlib.ZLIB_VERSION" title="永久链接至目标">¶</a></dt>
<dd><p>构建此模块时所用的 zlib 库的版本字符串。它的值可能与运行时所加载的 zlib 不同。运行时加载的 zlib 库的版本字符串为 <a class="reference internal" href="#zlib.ZLIB_RUNTIME_VERSION" title="zlib.ZLIB_RUNTIME_VERSION"><code class="xref py py-const docutils literal notranslate"><span class="pre">ZLIB_RUNTIME_VERSION</span></code></a>。</p>
</dd></dl>

<dl class="py data">
<dt id="zlib.ZLIB_RUNTIME_VERSION">
<code class="sig-prename descclassname">zlib.</code><code class="sig-name descname">ZLIB_RUNTIME_VERSION</code><a class="headerlink" href="#zlib.ZLIB_RUNTIME_VERSION" title="永久链接至目标">¶</a></dt>
<dd><p>解释器所加载的 zlib 库的版本字符串。</p>
<div class="versionadded">
<p><span class="versionmodified added">3.3 新版功能.</span></p>
</div>
</dd></dl>

<div class="admonition seealso">
<p class="admonition-title">参见</p>
<dl class="simple">
<dt>模块 <a class="reference internal" href="gzip.html#module-gzip" title="gzip: Interfaces for gzip compression and decompression using file objects."><code class="xref py py-mod docutils literal notranslate"><span class="pre">gzip</span></code></a></dt><dd><p>读写 <strong class="program">gzip</strong> 格式的文件。</p>
</dd>
<dt><a class="reference external" href="http://www.zlib.net">http://www.zlib.net</a></dt><dd><p>zlib 库项目主页。</p>
</dd>
<dt><a class="reference external" href="http://www.zlib.net/manual.html">http://www.zlib.net/manual.html</a></dt><dd><p>zlib 库用户手册。提供了库的许多功能的解释和用法。</p>
</dd>
</dl>
</div>
</section>


            <div class="clearer"></div>
          </div>
        </div>
      </div>
      <div class="sphinxsidebar" role="navigation" aria-label="main navigation">
        <div class="sphinxsidebarwrapper">
  <h4>上一个主题</h4>
  <p class="topless"><a href="archiving.html"
                        title="上一章">数据压缩和存档</a></p>
  <h4>下一个主题</h4>
  <p class="topless"><a href="gzip.html"
                        title="下一章"><code class="xref py py-mod docutils literal notranslate"><span class="pre">gzip</span></code> --- 对 <strong class="program">gzip</strong> 格式的支持</a></p>
  <div role="note" aria-label="source link">
    <h3>当前页面</h3>
    <ul class="this-page-menu">
      <li><a href="../bugs.html">提交 Bug</a></li>
      <li>
        <a href="https://github.com/python/cpython/blob/3.10/Doc/library/zlib.rst"
            rel="nofollow">显示源码
        </a>
      </li>
    </ul>
  </div>
        </div>
      </div>
      <div class="clearer"></div>
    </div>  
    <div class="related" role="navigation" aria-label="related navigation">
      <h3>导航</h3>
      <ul>
        <li class="right" style="margin-right: 10px">
          <a href="../genindex.html" title="总目录"
             >索引</a></li>
        <li class="right" >
          <a href="../py-modindex.html" title="Python 模块索引"
             >模块</a> |</li>
        <li class="right" >
          <a href="gzip.html" title="gzip --- 对 gzip 格式的支持"
             >下一页</a> |</li>
        <li class="right" >
          <a href="archiving.html" title="数据压缩和存档"
             >上一页</a> |</li>

          <li><img src="../_static/py.svg" alt="python logo" style="vertical-align: middle; margin-top: -1px"/></li>
          <li><a href="https://www.python.org/">Python</a> &#187;</li>
          <li class="switchers">
            <div class="language_switcher_placeholder"></div>
            <div class="version_switcher_placeholder"></div>
          </li>
          <li>
              
          </li>
    <li id="cpython-language-and-version">
      <a href="../index.html">3.10.8 Documentation</a> &#187;
    </li>

          <li class="nav-item nav-item-1"><a href="index.html" >Python 标准库</a> &#187;</li>
          <li class="nav-item nav-item-2"><a href="archiving.html" >数据压缩和存档</a> &#187;</li>
        <li class="nav-item nav-item-this"><a href=""><code class="xref py py-mod docutils literal notranslate"><span class="pre">zlib</span></code> --- 与 <strong class="program">gzip</strong> 兼容的压缩</a></li>
                <li class="right">
                    

    <div class="inline-search" role="search">
        <form class="inline-search" action="../search.html" method="get">
          <input placeholder="快速搜索" aria-label="快速搜索" type="text" name="q" />
          <input type="submit" value="转向" />
          <input type="hidden" name="check_keywords" value="yes" />
          <input type="hidden" name="area" value="default" />
        </form>
    </div>
                     |
                </li>
            
      </ul>
    </div>  
    <div class="footer">
    &copy; <a href="../copyright.html">版权所有</a> 2001-2022, Python Software Foundation.
    <br />
    This page is licensed under the Python Software Foundation License Version 2.
    <br />
    Examples, recipes, and other code in the documentation are additionally licensed under the Zero Clause BSD License.
    <br />
    See <a href="/license.html">History and License</a> for more information.<br />
    <br />

    The Python Software Foundation is a non-profit corporation.
<a href="https://www.python.org/psf/donations/">Please donate.</a>
<br />
    <br />

    最后更新于 11月 14, 2022.
    <a href="/bugs.html">Found a bug</a>?
    <br />

    Created using <a href="https://www.sphinx-doc.org/">Sphinx</a> 3.4.3.
    </div>

    <script type="text/javascript" src="../_static/switchers.js"></script>
  </body>
</html>"""
S2="""
<!DOCTYPE html>

<html lang="zh_CN">
  <head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" /><meta name="generator" content="Docutils 0.17.1: http://docutils.sourceforge.net/" />

    <title>zlib --- 与 gzip 兼容的压缩 &#8212; Python 3.10.8 文档</title><meta name="viewport" content="width=device-width, initial-scale=1.0">
    
    <link rel="stylesheet" href="../_static/pygments.css" type="text/css" />
    <link rel="stylesheet" href="../_static/pydoctheme.css?2022.1" type="text/css" />
    
    <script id="documentation_options" data-url_root="../" src="../_static/documentation_options.js"></script>
    <script src="../_static/jquery.js"></script>
    <script src="../_static/underscore.js"></script>
    <script src="../_static/doctools.js"></script>
    <script src="../_static/translations.js"></script>
    
    <script src="../_static/sidebar.js"></script>
    
    <link rel="search" type="application/opensearchdescription+xml"
          title="在 Python 3.10.8 文档 中搜索"
          href="../_static/opensearch.xml"/>
    <link rel="author" title="关于这些文档" href="../about.html" />
    <link rel="index" title="索引" href="../genindex.html" />
    <link rel="search" title="搜索" href="../search.html" />
    <link rel="copyright" title="版权所有" href="../copyright.html" />
    <link rel="next" title="gzip --- 对 gzip 格式的支持" href="gzip.html" />
    <link rel="prev" title="数据压缩和存档" href="archiving.html" />
    <link rel="canonical" href="https://docs.python.org/3/library/zlib.html" />
    
      
    

    
    <style>
      @media only screen {
        table.full-width-table {
            width: 100%;
        }
      }
    </style>
<link rel="shortcut icon" type="image/png" href="../_static/py.svg" />
            <script type="text/javascript" src="../_static/copybutton.js"></script>
            <script type="text/javascript" src="../_static/menu.js"></script> 

  </head>
<body>
<div class="mobile-nav">
    <input type="checkbox" id="menuToggler" class="toggler__input" aria-controls="navigation"
           aria-pressed="false" aria-expanded="false" role="button" aria-label="Menu" />
    <label for="menuToggler" class="toggler__label">
        <span></span>
    </label>
    <nav class="nav-content" role="navigation">
         <a href="https://www.python.org/" class="nav-logo">
             <img src="../_static/py.svg" alt="Logo"/>
         </a>
        <div class="version_switcher_placeholder"></div>
        <form role="search" class="search" action="../search.html" method="get">
            <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" class="search-icon">
                <path fill-rule="nonzero"
                        d="M15.5 14h-.79l-.28-.27a6.5 6.5 0 001.48-5.34c-.47-2.78-2.79-5-5.59-5.34a6.505 6.505 0 00-7.27 7.27c.34 2.8 2.56 5.12 5.34 5.59a6.5 6.5 0 005.34-1.48l.27.28v.79l4.25 4.25c.41.41 1.08.41 1.49 0 .41-.41.41-1.08 0-1.49L15.5 14zm-6 0C7.01 14 5 11.99 5 9.5S7.01 5 9.5 5 14 7.01 14 9.5 11.99 14 9.5 14z" fill="#444"></path>
            </svg>
            <input type="text" name="q" aria-label="快速搜索"/>
            <input type="submit" value="转向"/>
        </form>
    </nav>
    <div class="menu-wrapper">
        <nav class="menu" role="navigation" aria-label="main navigation">
            <div class="language_switcher_placeholder"></div>
  <h4>上一个主题</h4>
  <p class="topless"><a href="archiving.html"
                        title="上一章">数据压缩和存档</a></p>
  <h4>下一个主题</h4>
  <p class="topless"><a href="gzip.html"
                        title="下一章"><code class="xref py py-mod docutils literal notranslate"><span class="pre">gzip</span></code> --- 对 <strong class="program">gzip</strong> 格式的支持</a></p>
  <div role="note" aria-label="source link">
    <h3>当前页面</h3>
    <ul class="this-page-menu">
      <li><a href="../bugs.html">提交 Bug</a></li>
      <li>
        <a href="https://github.com/python/cpython/blob/3.10/Doc/library/zlib.rst"
            rel="nofollow">显示源码
        </a>
      </li>
    </ul>
  </div>
        </nav>
    </div>
</div>

  
    <div class="related" role="navigation" aria-label="related navigation">
      <h3>导航</h3>
      <ul>
        <li class="right" style="margin-right: 10px">
          <a href="../genindex.html" title="总目录"
             accesskey="I">索引</a></li>
        <li class="right" >
          <a href="../py-modindex.html" title="Python 模块索引"
             >模块</a> |</li>
        <li class="right" >
          <a href="gzip.html" title="gzip --- 对 gzip 格式的支持"
             accesskey="N">下一页</a> |</li>
        <li class="right" >
          <a href="archiving.html" title="数据压缩和存档"
             accesskey="P">上一页</a> |</li>

          <li><img src="../_static/py.svg" alt="python logo" style="vertical-align: middle; margin-top: -1px"/></li>
          <li><a href="https://www.python.org/">Python</a> &#187;</li>
          <li class="switchers">
            <div class="language_switcher_placeholder"></div>
            <div class="version_switcher_placeholder"></div>
          </li>
          <li>
              
          </li>
    <li id="cpython-language-and-version">
      <a href="../index.html">3.10.8 Documentation</a> &#187;
    </li>

          <li class="nav-item nav-item-1"><a href="index.html" >Python 标准库</a> &#187;</li>
          <li class="nav-item nav-item-2"><a href="archiving.html" accesskey="U">数据压缩和存档</a> &#187;</li>
        <li class="nav-item nav-item-this"><a href=""><code class="xref py py-mod docutils literal notranslate"><span class="pre">zlib</span></code> --- 与 <strong class="program">gzip</strong> 兼容的压缩</a></li>
                <li class="right">
                    

    <div class="inline-search" role="search">
        <form class="inline-search" action="../search.html" method="get">
          <input placeholder="快速搜索" aria-label="快速搜索" type="text" name="q" />
          <input type="submit" value="转向" />
          <input type="hidden" name="check_keywords" value="yes" />
          <input type="hidden" name="area" value="default" />
        </form>
    </div>
                     |
                </li>
            
      </ul>
    </div>    

    <div class="document">
      <div class="documentwrapper">
        <div class="bodywrapper">
          <div class="body" role="main">
            
  <section id="module-zlib">
<span id="zlib-compression-compatible-with-gzip"></span><h1><a class="reference internal" href="#module-zlib" title="zlib: Low-level interface to compression and decompression routines compatible with gzip."><code class="xref py py-mod docutils literal notranslate"><span class="pre">zlib</span></code></a> --- 与 <strong class="program">gzip</strong> 兼容的压缩<a class="headerlink" href="#module-zlib" title="永久链接至标题">¶</a></h1>
<hr class="docutils" />
<p>对于需要数据压缩的应用，此模块中的函数允许使用 zlib 库进行压缩和解压缩。 zlib 库的项目主页是 <a class="reference external" href="https://www.zlib.net">https://www.zlib.net</a>。 已知此 Python 模块与 1.1.3 之前版本的 zlib 库存在不兼容；1.1.3 版则存在一个 <a class="reference external" href="https://zlib.net/zlib_faq.html#faq33">安全缺陷</a>，因此我们推荐使用 1.1.4 或更新的版本。</p>
<p>zlib 的函数有很多选项，一般需要按特定顺序使用。本文档没有覆盖全部的用法。更多详细信息请于 <a class="reference external" href="http://www.zlib.net/manual.html">http://www.zlib.net/manual.html</a> 参阅官方手册。</p>
<p>要读写 <code class="docutils literal notranslate"><span class="pre">.gz</span></code> 格式的文件，请参考 <a class="reference internal" href="gzip.html#module-gzip" title="gzip: Interfaces for gzip compression and decompression using file objects."><code class="xref py py-mod docutils literal notranslate"><span class="pre">gzip</span></code></a> 模块。</p>
<p>此模块中可用的异常和函数如下：</p>
<dl class="py exception">
<dt id="zlib.error">
<em class="property">exception </em><code class="sig-prename descclassname">zlib.</code><code class="sig-name descname">error</code><a class="headerlink" href="#zlib.error" title="永久链接至目标">¶</a></dt>
<dd><p>在压缩或解压缩过程中发生错误时的异常。</p>
</dd></dl>

<dl class="py function">
<dt id="zlib.adler32">
<code class="sig-prename descclassname">zlib.</code><code class="sig-name descname">adler32</code><span class="sig-paren">(</span><em class="sig-param">data</em><span class="optional">[</span>, <em class="sig-param">value</em><span class="optional">]</span><span class="sig-paren">)</span><a class="headerlink" href="#zlib.adler32" title="永久链接至目标">¶</a></dt>
<dd><p>计算 <em>data</em> 的 Adler-32 校验值。(Adler-32 校验的可靠性与 CRC32 基本相当，但比计算 CRC32 更高效。) 计算的结果是一个 32 位的整数。参数 <em>value</em> 是校验时的起始值，其默认值为 1。借助参数 <em>value</em> 可为分段的输入计算校验值。此算法没有加密强度，不应用于身份验证和数字签名。此算法的目的仅为验证数据的正确性，不适合作为通用散列算法。</p>
<div class="versionchanged">
<p><span class="versionmodified changed">在 3.0 版更改: </span>结果值将始终为无符号类型。 要在使用 Python 2 或更早版本时生成同样的数值，请使用 <code class="docutils literal notranslate"><span class="pre">adler32(data)</span> <span class="pre">&amp;</span> <span class="pre">0xffffffff</span></code>。</p>
</div>
</dd></dl>

<dl class="py function">
<dt id="zlib.compress">
<code class="sig-prename descclassname">zlib.</code><code class="sig-name descname">compress</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">data</span></em>, <em class="sig-param"><span class="o">/</span></em>, <em class="sig-param"><span class="n">level</span><span class="o">=</span><span class="default_value">- 1</span></em><span class="sig-paren">)</span><a class="headerlink" href="#zlib.compress" title="永久链接至目标">¶</a></dt>
<dd><p>压缩 <em>data</em> 中的字节，返回含有已压缩内容的 bytes 对象。参数 <em>level</em> 为整数，可取值为 <code class="docutils literal notranslate"><span class="pre">0</span></code> 到 <code class="docutils literal notranslate"><span class="pre">9</span></code> 或 <code class="docutils literal notranslate"><span class="pre">-1</span></code>，用于指定压缩等级。<code class="docutils literal notranslate"><span class="pre">1</span></code> (Z_BEST_SPEED) 表示最快速度和最低压缩率，<code class="docutils literal notranslate"><span class="pre">9</span></code> (Z_BEST_COMPRESSION) 表示最慢速度和最高压缩率。<code class="docutils literal notranslate"><span class="pre">0</span></code> (Z_NO_COMPRESSION) 表示不压缩。参数默认值为 <code class="docutils literal notranslate"><span class="pre">-1</span></code> (Z_DEFAULT_COMPRESSION)。Z_DEFAULT_COMPRESSION 是速度和压缩率之间的平衡 (一般相当于设压缩等级为 6)。函数发生错误时抛出 <a class="reference internal" href="#zlib.error" title="zlib.error"><code class="xref py py-exc docutils literal notranslate"><span class="pre">error</span></code></a> 异常。</p>
<div class="versionchanged">
<p><span class="versionmodified changed">在 3.6 版更改: </span>现在，<em>level</em> 可作为关键字参数。</p>
</div>
</dd></dl>

<dl class="py function">
<dt id="zlib.compressobj">
<code class="sig-prename descclassname">zlib.</code><code class="sig-name descname">compressobj</code><span class="sig-paren">(</span><em class="sig-param">level=-1</em>, <em class="sig-param">method=DEFLATED</em>, <em class="sig-param">wbits=MAX_WBITS</em>, <em class="sig-param">memLevel=DEF_MEM_LEVEL</em>, <em class="sig-param">strategy=Z_DEFAULT_STRATEGY</em><span class="optional">[</span>, <em class="sig-param">zdict</em><span class="optional">]</span><span class="sig-paren">)</span><a class="headerlink" href="#zlib.compressobj" title="永久链接至目标">¶</a></dt>
<dd><p>返回一个 压缩对象，用来压缩内存中难以容下的数据流。</p>
<p>参数 <em>level</em> 为压缩等级，是整数，可取值为 <code class="docutils literal notranslate"><span class="pre">0</span></code> 到 <code class="docutils literal notranslate"><span class="pre">9</span></code> 或 <code class="docutils literal notranslate"><span class="pre">-1</span></code>。<code class="docutils literal notranslate"><span class="pre">1</span></code> (Z_BEST_SPEED) 表示最快速度和最低压缩率，<code class="docutils literal notranslate"><span class="pre">9</span></code> (Z_BEST_COMPRESSION) 表示最慢速度和最高压缩率。<code class="docutils literal notranslate"><span class="pre">0</span></code> (Z_NO_COMPRESSION) 表示不压缩。参数默认值为 <code class="docutils literal notranslate"><span class="pre">-1</span></code> (Z_DEFAULT_COMPRESSION)。Z_DEFAULT_COMPRESSION 是速度和压缩率之间的平衡 (一般相当于设压缩等级为 6)。</p>
<p><em>method</em> 表示压缩算法。现在只支持 <code class="xref py py-const docutils literal notranslate"><span class="pre">DEFLATED</span></code> 这个算法。</p>
<p>参数 <em>wbits</em> 指定压缩数据时所使用的历史缓冲区的大小 (窗口大小)，并指定压缩输出是否包含头部或尾部。参数的默认值是 <code class="docutils literal notranslate"><span class="pre">15</span></code> (MAX_WBITS)。参数的值分为几个范围：</p>
<ul class="simple">
<li><p>+9 至 +15：窗口大小以二为底的对数。 即这些值对应着 512 至 32768 的窗口大小。 更大的值会提供更好的压缩，同时内存开销也会更大。 压缩输出会包含 zlib 特定格式的头部和尾部。</p></li>
<li><p>−9 至 −15：绝对值为窗口大小以二为底的对数。 压缩输出仅包含压缩数据，没有头部和尾部。</p></li>
<li><p>+25 至 +31 = 16 + (9 至 15)：后 4 个比特位为窗口大小以二为底的对数。 压缩输出包含一个基本的 <strong class="program">gzip</strong> 头部，并以校验和为尾部。</p></li>
</ul>
<p>参数 <em>memLevel</em> 指定内部压缩操作时所占用内存大小。参数取 <code class="docutils literal notranslate"><span class="pre">1</span></code> 到 <code class="docutils literal notranslate"><span class="pre">9</span></code>。更大的值占用更多的内存，同时速度也更快输出也更小。</p>
<p>参数 <em>strategy</em> 用于调节压缩算法。可取值为  <code class="xref py py-const docutils literal notranslate"><span class="pre">Z_DEFAULT_STRATEGY</span></code>、<code class="xref py py-const docutils literal notranslate"><span class="pre">Z_FILTERED</span></code>、<code class="xref py py-const docutils literal notranslate"><span class="pre">Z_HUFFMAN_ONLY</span></code>、<code class="xref py py-const docutils literal notranslate"><span class="pre">Z_RLE</span></code> (zlib 1.2.0.1) 或 <code class="xref py py-const docutils literal notranslate"><span class="pre">Z_FIXED</span></code> (zlib 1.2.2.2)。</p>
<p>参数 <em>zdict</em> 指定预定义的压缩字典。它是一个字节序列 (如 <a class="reference internal" href="stdtypes.html#bytes" title="bytes"><code class="xref py py-class docutils literal notranslate"><span class="pre">bytes</span></code></a> 对象)，其中包含用户认为要压缩的数据中可能频繁出现的子序列。频率高的子序列应当放在字典的尾部。</p>
<div class="versionchanged">
<p><span class="versionmodified changed">在 3.3 版更改: </span>添加关键字参数 <em>zdict</em>。</p>
</div>
</dd></dl>

<dl class="py function">
<dt id="zlib.crc32">
<code class="sig-prename descclassname">zlib.</code><code class="sig-name descname">crc32</code><span class="sig-paren">(</span><em class="sig-param">data</em><span class="optional">[</span>, <em class="sig-param">value</em><span class="optional">]</span><span class="sig-paren">)</span><a class="headerlink" href="#zlib.crc32" title="永久链接至目标">¶</a></dt>
<dd><p id="index-0">计算 <em>data</em> 的 CRC (循环冗余校验) 值。计算的结果是一个 32 位的整数。参数 <em>value</em> 是校验时的起始值，其默认值为 0。借助参数 <em>value</em> 可为分段的输入计算校验值。此算法没有加密强度，不应用于身份验证和数字签名。此算法的目的仅为验证数据的正确性，不适合作为通用散列算法。</p>
<div class="versionchanged">
<p><span class="versionmodified changed">在 3.0 版更改: </span>结果值将始终为无符号类型。 要在使用 Python 2 或更早版本时生成同样的数值，请使用 <code class="docutils literal notranslate"><span class="pre">crc32(data)</span> <span class="pre">&amp;</span> <span class="pre">0xffffffff</span></code>。</p>
</div>
</dd></dl>

<dl class="py function">
<dt id="zlib.decompress">
<code class="sig-prename descclassname">zlib.</code><code class="sig-name descname">decompress</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">data</span></em>, <em class="sig-param"><span class="o">/</span></em>, <em class="sig-param"><span class="n">wbits</span><span class="o">=</span><span class="default_value">MAX_WBITS</span></em>, <em class="sig-param"><span class="n">bufsize</span><span class="o">=</span><span class="default_value">DEF_BUF_SIZE</span></em><span class="sig-paren">)</span><a class="headerlink" href="#zlib.decompress" title="永久链接至目标">¶</a></dt>
<dd><p>解压 <em>data</em> 中的字节，返回含有已解压内容的 bytes 对象。参数 <em>wbits</em> 取决于 <em>data</em> 的格式，具体参见下边的说明。<em>bufsize</em> 为输出缓冲区的起始大小。函数发生错误时抛出 <a class="reference internal" href="#zlib.error" title="zlib.error"><code class="xref py py-exc docutils literal notranslate"><span class="pre">error</span></code></a> 异常。</p>
<p id="decompress-wbits"><em>wbits</em> 形参控制历史缓冲区的大小（或称“窗口大小”）以及所期望的头部和尾部格式。 它类似于 <a class="reference internal" href="#zlib.compressobj" title="zlib.compressobj"><code class="xref py py-func docutils literal notranslate"><span class="pre">compressobj()</span></code></a> 的形参，但可接受更大范围的值：</p>
<ul class="simple">
<li><p>+8 至 +15：窗口尺寸以二为底的对数。 输入必须包含 zlib 头部和尾部。</p></li>
<li><p>0：根据 zlib 头部自动确定窗口大小。 只从 zlib 1.2.3.5 版起受支持。</p></li>
<li><p>−8 至 −15：使用 <em>wbits</em> 的绝对值作为窗口大小以二为底的对数。 输入必须为原始数据流，没有头部和尾部。</p></li>
<li><p>+24 至 +31 = 16 + (8 至 15)：使用后 4 个比特位作为窗口大小以二为底的对数。 输入必须包括 gzip 头部和尾部。</p></li>
<li><p>+40 至 +47 = 32 + (8 至 15)：使用后 4 个比特位作为窗口大小以二为底的对数，并且自动接受 zlib 或 gzip 格式。</p></li>
</ul>
<p>当解压缩一个数据流时，窗口大小必须不小于用于压缩数据流的原始窗口大小；使用太小的值可能导致 <a class="reference internal" href="#zlib.error" title="zlib.error"><code class="xref py py-exc docutils literal notranslate"><span class="pre">error</span></code></a> 异常。 默认 <em>wbits</em> 值对应于最大的窗口大小并且要求包括 zlib 头部和尾部。</p>
<p><em>bufsize</em> 是用于存放解压数据的缓冲区初始大小。 如果需要更大空间，缓冲区大小将按需增加，因此你不需要让这个值完全精确；对其进行调整仅会节省一点对 <code class="xref c c-func docutils literal notranslate"><span class="pre">malloc()</span></code> 的调用次数。</p>
<div class="versionchanged">
<p><span class="versionmodified changed">在 3.6 版更改: </span><em>wbits</em> 和 <em>bufsize</em> 可用作关键字参数。</p>
</div>
</dd></dl>

<dl class="py function">
<dt id="zlib.decompressobj">
<code class="sig-prename descclassname">zlib.</code><code class="sig-name descname">decompressobj</code><span class="sig-paren">(</span><em class="sig-param">wbits=MAX_WBITS</em><span class="optional">[</span>, <em class="sig-param">zdict</em><span class="optional">]</span><span class="sig-paren">)</span><a class="headerlink" href="#zlib.decompressobj" title="永久链接至目标">¶</a></dt>
<dd><p>返回一个解压对象，用来解压无法被一次性放入内存的数据流。</p>
<p><em>wbits</em> 形参控制历史缓冲区的大小（或称“窗口大小”）以及所期望的头部和尾部格式。 它的含义与 <a class="reference external" href="#decompress-wbits">对 decompress() 的描述</a> 相同。</p>
<p><em>zdict</em> 形参指定指定一个预定义的压缩字典。 如果提供了此形参，它必须与产生将解压数据的压缩器所使用的字典相同。</p>
<div class="admonition note">
<p class="admonition-title">注解</p>
<p>如果 <em>zdict</em> 是一个可变对象 (例如 <a class="reference internal" href="stdtypes.html#bytearray" title="bytearray"><code class="xref py py-class docutils literal notranslate"><span class="pre">bytearray</span></code></a>)，则你不可在对 <a class="reference internal" href="#zlib.decompressobj" title="zlib.decompressobj"><code class="xref py py-func docutils literal notranslate"><span class="pre">decompressobj()</span></code></a> 的调用和对解压器的 <code class="docutils literal notranslate"><span class="pre">decompress()</span></code> 方法的调用之间修改其内容。</p>
</div>
<div class="versionchanged">
<p><span class="versionmodified changed">在 3.3 版更改: </span>增加了 <em>zdict</em> 形参。</p>
</div>
</dd></dl>

<p>压缩对象支持以下方法：</p>
<dl class="py method">
<dt id="zlib.Compress.compress">
<code class="sig-prename descclassname">Compress.</code><code class="sig-name descname">compress</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">data</span></em><span class="sig-paren">)</span><a class="headerlink" href="#zlib.Compress.compress" title="永久链接至目标">¶</a></dt>
<dd><p>压缩 <em>data</em> 并返回 bytes 对象，这个对象含有 <em>data</em> 的部分或全部内容的已压缩数据。所得的对象必须拼接在上一次调用 <a class="reference internal" href="#zlib.compress" title="zlib.compress"><code class="xref py py-meth docutils literal notranslate"><span class="pre">compress()</span></code></a> 方法所得数据的后面。缓冲区中可能留存部分输入以供下一次调用。</p>
</dd></dl>

<dl class="py method">
<dt id="zlib.Compress.flush">
<code class="sig-prename descclassname">Compress.</code><code class="sig-name descname">flush</code><span class="sig-paren">(</span><span class="optional">[</span><em class="sig-param">mode</em><span class="optional">]</span><span class="sig-paren">)</span><a class="headerlink" href="#zlib.Compress.flush" title="永久链接至目标">¶</a></dt>
<dd><p>压缩所有缓冲区的数据并返回已压缩的数据。参数 <em>mode</em> 可以传入的常量为：<code class="xref py py-const docutils literal notranslate"><span class="pre">Z_NO_FLUSH</span></code>、<code class="xref py py-const docutils literal notranslate"><span class="pre">Z_PARTIAL_FLUSH</span></code>、<code class="xref py py-const docutils literal notranslate"><span class="pre">Z_SYNC_FLUSH</span></code>、<code class="xref py py-const docutils literal notranslate"><span class="pre">Z_FULL_FLUSH</span></code>、<code class="xref py py-const docutils literal notranslate"><span class="pre">Z_BLOCK</span></code> (zlib 1.2.3.4) 或 <code class="xref py py-const docutils literal notranslate"><span class="pre">Z_FINISH</span></code>。默认值为 <code class="xref py py-const docutils literal notranslate"><span class="pre">Z_FINISH</span></code>。<code class="xref py py-const docutils literal notranslate"><span class="pre">Z_FINISH</span></code> 关闭已压缩数据流并不允许再压缩其他数据，<code class="xref py py-const docutils literal notranslate"><span class="pre">Z_FINISH</span></code>  以外的值皆允许这个对象继续压缩数据。调用 <a class="reference internal" href="#zlib.Compress.flush" title="zlib.Compress.flush"><code class="xref py py-meth docutils literal notranslate"><span class="pre">flush()</span></code></a> 方法并将 <em>mode</em> 设为 <code class="xref py py-const docutils literal notranslate"><span class="pre">Z_FINISH</span></code> 后会无法再次调用 <a class="reference internal" href="#zlib.compress" title="zlib.compress"><code class="xref py py-meth docutils literal notranslate"><span class="pre">compress()</span></code></a>，此时只能删除这个对象。</p>
</dd></dl>

<dl class="py method">
<dt id="zlib.Compress.copy">
<code class="sig-prename descclassname">Compress.</code><code class="sig-name descname">copy</code><span class="sig-paren">(</span><span class="sig-paren">)</span><a class="headerlink" href="#zlib.Compress.copy" title="永久链接至目标">¶</a></dt>
<dd><p>返回此压缩对象的一个拷贝。它可以用来高效压缩一系列拥有相同前缀的数据。</p>
</dd></dl>

<div class="versionchanged">
<p><span class="versionmodified changed">在 3.8 版更改: </span>添加了对压缩对象执行 <a class="reference internal" href="copy.html#copy.copy" title="copy.copy"><code class="xref py py-func docutils literal notranslate"><span class="pre">copy.copy()</span></code></a> 和 <a class="reference internal" href="copy.html#copy.deepcopy" title="copy.deepcopy"><code class="xref py py-func docutils literal notranslate"><span class="pre">copy.deepcopy()</span></code></a> 的支持。</p>
</div>
<p>解压缩对象支持以下方法：</p>
<dl class="py attribute">
<dt id="zlib.Decompress.unused_data">
<code class="sig-prename descclassname">Decompress.</code><code class="sig-name descname">unused_data</code><a class="headerlink" href="#zlib.Decompress.unused_data" title="永久链接至目标">¶</a></dt>
<dd><p>一个 bytes 对象，其中包含压缩数据结束之后的任何字节数据。 也就是说，它将为 <code class="docutils literal notranslate"><span class="pre">b&quot;&quot;</span></code> 直到包含压缩数据的末尾字节可用。 如果整个结果字节串都包含压缩数据，它将为一个空的 bytes 对象 <code class="docutils literal notranslate"><span class="pre">b&quot;&quot;</span></code>。</p>
</dd></dl>

<dl class="py attribute">
<dt id="zlib.Decompress.unconsumed_tail">
<code class="sig-prename descclassname">Decompress.</code><code class="sig-name descname">unconsumed_tail</code><a class="headerlink" href="#zlib.Decompress.unconsumed_tail" title="永久链接至目标">¶</a></dt>
<dd><p>一个 bytes 对象，其中包含未被上一次 <a class="reference internal" href="#zlib.decompress" title="zlib.decompress"><code class="xref py py-meth docutils literal notranslate"><span class="pre">decompress()</span></code></a> 调用所消耗的任何数据。 此数据不能被 zlib 机制看到，因此你必须将其送回（可能要附带额外的数据拼接）到后续的 <a class="reference internal" href="#zlib.decompress" title="zlib.decompress"><code class="xref py py-meth docutils literal notranslate"><span class="pre">decompress()</span></code></a> 方法调用以获得正确的输出。</p>
</dd></dl>

<dl class="py attribute">
<dt id="zlib.Decompress.eof">
<code class="sig-prename descclassname">Decompress.</code><code class="sig-name descname">eof</code><a class="headerlink" href="#zlib.Decompress.eof" title="永久链接至目标">¶</a></dt>
<dd><p>一个布尔值，指明是否已到达压缩数据流的末尾。</p>
<p>This makes it possible to distinguish between a properly formed compressed
stream, and an incomplete or truncated one.</p>
<div class="versionadded">
<p><span class="versionmodified added">3.3 新版功能.</span></p>
</div>
</dd></dl>

<dl class="py method">
<dt id="zlib.Decompress.decompress">
<code class="sig-prename descclassname">Decompress.</code><code class="sig-name descname">decompress</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">data</span></em>, <em class="sig-param"><span class="n">max_length</span><span class="o">=</span><span class="default_value">0</span></em><span class="sig-paren">)</span><a class="headerlink" href="#zlib.Decompress.decompress" title="永久链接至目标">¶</a></dt>
<dd><p>解压缩 <em>data</em> 并返回 bytes 对象，其中包含对应于 <em>string</em> 中至少一部分数据的解压缩数据。 此数据应当被拼接到之前任何对 <a class="reference internal" href="#zlib.decompress" title="zlib.decompress"><code class="xref py py-meth docutils literal notranslate"><span class="pre">decompress()</span></code></a> 方法的调用所产生的输出。 部分输入数据可能会被保留在内部缓冲区以供后续处理。</p>
<p>如果可选的形参 <em>max_length</em> 非零则返回值将不会长于 <em>max_length</em>。 这可能意味着不是所有已压缩输入都能被处理；并且未被消耗的数据将被保存在 <a class="reference internal" href="#zlib.Decompress.unconsumed_tail" title="zlib.Decompress.unconsumed_tail"><code class="xref py py-attr docutils literal notranslate"><span class="pre">unconsumed_tail</span></code></a> 属性中。 如果要继续解压缩则这个字节串必须被传给对 <a class="reference internal" href="#zlib.decompress" title="zlib.decompress"><code class="xref py py-meth docutils literal notranslate"><span class="pre">decompress()</span></code></a> 的后续调用。 如果 <em>max_length</em> 为零则整个输入都会被解压缩，并且 <a class="reference internal" href="#zlib.Decompress.unconsumed_tail" title="zlib.Decompress.unconsumed_tail"><code class="xref py py-attr docutils literal notranslate"><span class="pre">unconsumed_tail</span></code></a> 将为空。</p>
<div class="versionchanged">
<p><span class="versionmodified changed">在 3.6 版更改: </span><em>max_length</em> 可用作关键字参数。</p>
</div>
</dd></dl>

<dl class="py method">
<dt id="zlib.Decompress.flush">
<code class="sig-prename descclassname">Decompress.</code><code class="sig-name descname">flush</code><span class="sig-paren">(</span><span class="optional">[</span><em class="sig-param">length</em><span class="optional">]</span><span class="sig-paren">)</span><a class="headerlink" href="#zlib.Decompress.flush" title="永久链接至目标">¶</a></dt>
<dd><p>所有挂起的输入会被处理，并且返回包含剩余未压缩输出的 bytes 对象。 在调用 <a class="reference internal" href="#zlib.Decompress.flush" title="zlib.Decompress.flush"><code class="xref py py-meth docutils literal notranslate"><span class="pre">flush()</span></code></a> 之后，<a class="reference internal" href="#zlib.decompress" title="zlib.decompress"><code class="xref py py-meth docutils literal notranslate"><span class="pre">decompress()</span></code></a> 方法将无法被再次调用；唯一可行的操作是删除该对象。</p>
<p>可选的形参 <em>length</em> 设置输出缓冲区的初始大小。</p>
</dd></dl>

<dl class="py method">
<dt id="zlib.Decompress.copy">
<code class="sig-prename descclassname">Decompress.</code><code class="sig-name descname">copy</code><span class="sig-paren">(</span><span class="sig-paren">)</span><a class="headerlink" href="#zlib.Decompress.copy" title="永久链接至目标">¶</a></dt>
<dd><p>返回解压缩对象的一个拷贝。 它可以用来在数据流的中途保存解压缩器的状态以便加快随机查找数据流后续位置的速度。</p>
</dd></dl>

<div class="versionchanged">
<p><span class="versionmodified changed">在 3.8 版更改: </span>添加了对解压缩对象执行 <a class="reference internal" href="copy.html#copy.copy" title="copy.copy"><code class="xref py py-func docutils literal notranslate"><span class="pre">copy.copy()</span></code></a> 和 <a class="reference internal" href="copy.html#copy.deepcopy" title="copy.deepcopy"><code class="xref py py-func docutils literal notranslate"><span class="pre">copy.deepcopy()</span></code></a> 的支持。</p>
</div>
<p>通过下列常量可获取模块所使用的 zlib 库的版本信息：</p>
<dl class="py data">
<dt id="zlib.ZLIB_VERSION">
<code class="sig-prename descclassname">zlib.</code><code class="sig-name descname">ZLIB_VERSION</code><a class="headerlink" href="#zlib.ZLIB_VERSION" title="永久链接至目标">¶</a></dt>
<dd><p>构建此模块时所用的 zlib 库的版本字符串。它的值可能与运行时所加载的 zlib 不同。运行时加载的 zlib 库的版本字符串为 <a class="reference internal" href="#zlib.ZLIB_RUNTIME_VERSION" title="zlib.ZLIB_RUNTIME_VERSION"><code class="xref py py-const docutils literal notranslate"><span class="pre">ZLIB_RUNTIME_VERSION</span></code></a>。</p>
</dd></dl>

<dl class="py data">
<dt id="zlib.ZLIB_RUNTIME_VERSION">
<code class="sig-prename descclassname">zlib.</code><code class="sig-name descname">ZLIB_RUNTIME_VERSION</code><a class="headerlink" href="#zlib.ZLIB_RUNTIME_VERSION" title="永久链接至目标">¶</a></dt>
<dd><p>解释器所加载的 zlib 库的版本字符串。</p>
<div class="versionadded">
<p><span class="versionmodified added">3.3 新版功能.</span></p>
</div>
</dd></dl>

<div class="admonition seealso">
<p class="admonition-title">参见</p>
<dl class="simple">
<dt>模块 <a class="reference internal" href="gzip.html#module-gzip" title="gzip: Interfaces for gzip compression and decompression using file objects."><code class="xref py py-mod docutils literal notranslate"><span class="pre">gzip</span></code></a></dt><dd><p>读写 <strong class="program">gzip</strong> 格式的文件。</p>
</dd>
<dt><a class="reference external" href="http://www.zlib.net">http://www.zlib.net</a></dt><dd><p>zlib 库项目主页。</p>
</dd>
<dt><a class="reference external" href="http://www.zlib.net/manual.html">http://www.zlib.net/manual.html</a></dt><dd><p>zlib 库用户手册。提供了库的许多功能的解释和用法。</p>
</dd>
</dl>
</div>
</section>


            <div class="clearer"></div>
          </div>
        </div>
      </div>
      <div class="sphinxsidebar" role="navigation" aria-label="main navigation">
        <div class="sphinxsidebarwrapper">
  <h4>上一个主题</h4>
  <p class="topless"><a href="archiving.html"
                        title="上一章">数据压缩和存档</a></p>
  <h4>下一个主题</h4>
  <p class="topless"><a href="gzip.html"
                        title="下一章"><code class="xref py py-mod docutils literal notranslate"><span class="pre">gzip</span></code> --- 对 <strong class="program">gzip</strong> 格式的支持</a></p>
  <div role="note" aria-label="source link">
    <h3>当前页面</h3>
    <ul class="this-page-menu">
      <li><a href="../bugs.html">提交 Bug</a></li>
      <li>
        <a href="https://github.com/python/cpython/blob/3.10/Doc/library/zlib.rst"
            rel="nofollow">显示源码
        </a>
      </li>
    </ul>
  </div>
        </div>
      </div>
      <div class="clearer"></div>
    </div>  
    <div class="related" role="navigation" aria-label="related navigation">
      <h3>导航</h3>
      <ul>
        <li class="right" style="margin-right: 10px">
          <a href="../genindex.html" title="总目录"
             >索引</a></li>
        <li class="right" >
          <a href="../py-modindex.html" title="Python 模块索引"
             >模块</a> |</li>
        <li class="right" >
          <a href="gzip.html" title="gzip --- 对 gzip 格式的支持"
             >下一页</a> |</li>
        <li class="right" >
          <a href="archiving.html" title="数据压缩和存档"
             >上一页</a> |</li>

          <li><img src="../_static/py.svg" alt="python logo" style="vertical-align: middle; margin-top: -1px"/></li>
          <li><a href="https://www.python.org/">Python</a> &#187;</li>
          <li class="switchers">
            <div class="language_switcher_placeholder"></div>
            <div class="version_switcher_placeholder"></div>
          </li>
          <li>
              
          </li>
    <li id="cpython-language-and-version">
      <a href="../index.html">3.10.8 Documentation</a> &#187;
    </li>

          <li class="nav-item nav-item-1"><a href="index.html" >Python 标准库</a> &#187;</li>
          <li class="nav-item nav-item-2"><a href="archiving.html" >数据压缩和存档</a> &#187;</li>
        <li class="nav-item nav-item-this"><a href=""><code class="xref py py-mod docutils literal notranslate"><span class="pre">zlib</span></code> --- 与 <strong class="program">gzip</strong> 兼容的压缩</a></li>
                <li class="right">
                    

    <div class="inline-search" role="search">
        <form class="inline-search" action="../search.html" method="get">
          <input placeholder="快速搜索" aria-label="快速搜索" type="text" name="q" />
          <input type="submit" value="转向" />
          <input type="hidden" name="check_keywords" value="yes" />
          <input type="hidden" name="area" value="default" />
        </form>
    </div>
                     |
                </li>
            
      </ul>
    </div>  
    <div class="footer">
    &copy; <a href="../copyright.html">版权所有</a> 2001-2022, Python Software Foundation.
    <br />
    This page is licensed under the Python Software Foundation License Version 2.
    <br />
    Examples, recipes, and other code in the documentation are additionally licensed under the Zero Clause BSD License.
    <br />
    See <a href="/license.html">History and License</a> for more information.<br />
    <br />

    The Python Software Foundation is a non-profit corporation.
<a href="https://www.python.org/psf/donations/">Please donate.</a>
<br />
    <br />

    最后更新于 11月 14, 2022.
    <a href="/bugs.html">Found a bug</a>?
    <br />

    Created using <a href="https://www.sphinx-doc.org/">Sphinx</a> 3.4.3.
    </div>

    <script type="text/javascript" src="../_static/switchers.js"></script>
  </body>
</html>"""
print(S1==S2,S1 is S2)

