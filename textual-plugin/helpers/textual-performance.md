# textual-performance

Performance optimization techniques, profiling tools, monitoring strategies, and performance best practices for Textual applications.

## Overview

Textual applications can achieve excellent performance, but like any UI framework, they require understanding of performance characteristics and optimization techniques. This guide covers performance optimization for TUI applications.

## Performance Fundamentals

### Performance Considerations

1. **Rendering Speed**: How quickly the UI updates
2. **Memory Usage**: Widget and data structure memory footprint
3. **Event Handling**: Event processing latency
4. **Data Binding**: Reactive property update efficiency
5. **Screen Updates**: DOM update frequency and batching

### Performance Measurement

```python
import time
import cProfile
import pstats
from functools import wraps

def profile(fn):
    """Decorator to profile function."""
    @wraps(fn)
    def wrapper(*args, **kwargs):
        pr = cProfile.Profile()
        pr.enable()
        result = fn(*args, **kwargs)
        pr.disable()

        # Save stats
        stats = pstats.Stats(pr)
        stats.sort_stats('cumulative')
        stats.print_stats(10)  # Top 10 functions

        return result
    return wrapper

class PerformanceMonitor:
    """Monitor app performance."""

    def __init__(self, app):
        self.app = app
        self.render_times = []
        self.update_times = []
        self.message_times = []

    def log_render_time(self, duration: float):
        """Log render time."""
        self.render_times.append(duration)
        if len(self.render_times) > 100:
            self.render_times.pop(0)

        # Alert if too slow
        if duration > 0.1:  # 100ms
            self.app.log(f"Slow render: {duration:.3f}s")

    def get_stats(self) -> dict:
        """Get performance statistics."""
        if not self.render_times:
            return {}

        return {
            "avg_render_time": sum(self.render_times) / len(self.render_times),
            "max_render_time": max(self.render_times),
            "min_render_time": min(self.render_times),
            "total_renders": len(self.render_times),
        }

# Usage
class MyApp(App):
    def on_mount(self) -> None:
        self.performance = PerformanceMonitor(self)

    def on_key(self, event) -> None:
        start = time.time()
        # Handle key
        duration = time.time() - start
        self.performance.log_message_time(duration)
```

## Rendering Optimization

### Reduce DOM Updates

```python
# Bad: Frequent DOM updates
class InefficientApp(App):
    def __init__(self):
        super().__init__()
        self.count = 0

    def compose(self):
        yield Static("", id="display")

    def on_mount(self) -> None:
        # Update every frame
        self.set_interval(0.001, self.increment)

    def increment(self):
        self.count += 1
        # This triggers a DOM update every time!
        display = self.query_one("#display", Static)
        display.update(str(self.count))

# Good: Batch updates
class EfficientApp(App):
    def __init__(self):
        super().__init__()
        self.count = 0
        self.pending_update = False

    def compose(self):
        yield Static("0", id="display")

    def on_mount(self) -> None:
        self.set_interval(0.001, self.increment)

    def increment(self):
        self.count += 1
        # Only schedule one update
        if not self.pending_update:
            self.pending_update = True
            # Schedule update for next frame
            self.call_after_refresh(self.update_display)

    def update_display(self):
        """Single DOM update."""
        self.pending_update = False
        display = self.query_one("#display", Static)
        display.update(str(self.count))
```

### Optimize Widget Rendering

```python
# Good: Efficient custom widget
class OptimizedWidget(Widget):
    """Efficient widget that only updates when needed."""

    def __init__(self):
        super().__init__()
        self._cache = None  # Cache rendered content
        self._last_update = 0

    def render(self):
        """Only re-render if data changed."""
        current = self.get_data()
        if current != self._cache:
            self._cache = current
            return current
        return self._cache  # Return cached

    def get_data(self):
        """Get data to render."""
        # Expensive operation here
        return self.app.data if hasattr(self.app, 'data') else None

    def on_mount(self) -> None:
        """Use refresh to avoid full re-render."""
        # Instead of update(), use refresh() for subtle changes
        self.refresh()
```

### Avoid Expensive Render Operations

```python
# Bad: Expensive rendering
def render(self):
    """Expensive render operation."""
    result = []
    for item in self.expensive_dataset:  # Large dataset
        # Complex formatting
        formatted = f"{item['name']:20} | {item['value']:10}"
        result.append(formatted)
    return "\n".join(result)

# Good: Cached rendering
class CachedRenderer(Widget):
    def __init__(self):
        super().__init__()
        self._cached_output = None
        self._cached_data = None

    def render(self):
        """Efficient rendering with caching."""
        current_data = self.get_data()

        # Only re-render if data changed
        if current_data != self._cached_data:
            self._cached_data = current_data
            self._cached_output = self.format_data(current_data)

        return self._cached_output

    def format_data(self, data):
        """Format data efficiently."""
        # Use generator for large datasets
        return "\n".join(
            f"{item['name']:20} | {item['value']:10}"
            for item in data
        )
```

## Data Structure Optimization

### Efficient Data Models

```python
# Good: Efficient data structure
class EfficientModel:
    """Model with efficient data handling."""

    def __init__(self):
        # Use appropriate data structures
        self._items = {}  # Dict for O(1) lookup
        self._ordered_items = []  # List for ordered access
        self._index = {}  # Index for fast queries

    def add_item(self, item):
        """Add item efficiently."""
        self._items[item.id] = item
        self._ordered_items.append(item)
        # Update index
        if hasattr(item, 'category'):
            self._index.setdefault(item.category, []).append(item)

    def get_item(self, item_id):
        """Get item in O(1) time."""
        return self._items.get(item_id)

    def get_items_by_category(self, category):
        """Get items by category from index."""
        return self._index.get(category, [])

    def get_all_items(self):
        """Get all items in order."""
        return self._ordered_items

# Bad: Inefficient data access
class InefficientModel:
    """Inefficient model with slow lookups."""

    def __init__(self):
        self.items = []  # List for all operations

    def add_item(self, item):
        """O(n) append."""
        self.items.append(item)

    def get_item(self, item_id):
        """O(n) lookup."""
        for item in self.items:
            if item.id == item_id:
                return item
        return None

    def get_items_by_category(self, category):
        """O(n) filter."""
        return [item for item in self.items if item.category == category]
```

### Memory Management

```python
class MemoryEfficientApp(App):
    """App with memory-efficient patterns."""

    def __init__(self):
        super().__init__()
        self._data_cache = None
        self._cache_timestamp = 0
        self._cache_duration = 5.0  # Cache for 5 seconds

    def get_cached_data(self):
        """Get data with caching."""
        import time

        current_time = time.time()

        # Return cache if valid
        if self._data_cache and (current_time - self._cache_timestamp) < self._cache_duration:
            return self._data_cache

        # Fetch fresh data
        self._data_cache = self.fetch_data()
        self._cache_timestamp = current_time
        return self._data_cache

    def clear_cache(self):
        """Clear data cache."""
        self._data_cache = None
        self._cache_timestamp = 0

    def on_unmount(self) -> None:
        """Clean up on unmount."""
        self.clear_cache()
        # Clean up other resources
        super().on_unmount()

# Use weak references for callbacks
import weakref

class CallbackManager:
    """Manage callbacks with weak references."""

    def __init__(self):
        self._callbacks = weakref.WeakSet()

    def add_callback(self, callback):
        """Add callback without preventing garbage collection."""
        self._callbacks.add(callback)

    def notify(self):
        """Notify all callbacks."""
        for callback in self._callbacks:
            try:
                callback()
            except Exception:
                pass  # Handle callback errors
```

### Lazy Loading

```python
class LazyDataManager:
    """Lazy data loading."""

    def __init__(self):
        self._data = None
        self._loaded = False
        self._loading = False

    def get_data(self):
        """Get data, loading only when needed."""
        if not self._loaded and not self._loading:
            self._loading = True
            # Start async load
            self.load_data()
        return self._data

    async def load_data(self):
        """Load data asynchronously."""
        try:
            # Simulate async load
            await asyncio.sleep(0.1)
            self._data = self.fetch_from_source()
            self._loaded = True
        finally:
            self._loading = False

class LazyWidget(Widget):
    """Widget with lazy data loading."""

    def compose(self):
        yield Static("Loading...", id="status")

    def on_mount(self) -> None:
        """Start lazy load."""
        self.data_manager = LazyDataManager()
        self.set_timer(0.1, self.load_data)

    def load_data(self):
        """Load data asynchronously."""
        import asyncio

        async def fetch():
            data = await self.data_manager.get_data()
            if data:
                self.query_one("#status", Static).update(f"Loaded {len(data)} items")

        asyncio.create_task(fetch())
```

## Event Handling Optimization

### Debouncing Events

```python
import time

class Debouncer:
    """Event debouncer to reduce event frequency."""

    def __init__(self, delay: float, callback):
        self.delay = delay
        self.callback = callback
        self.timer = None
        self.pending_args = None

    def __call__(self, *args, **kwargs):
        """Debounced function call."""
        # Cancel previous timer
        if self.timer:
            self.timer.stop()

        # Store latest arguments
        self.pending_args = (args, kwargs)

        # Schedule new timer
        self.timer = self.set_timer(self.delay, self._execute)

    def _execute(self):
        """Execute callback with latest arguments."""
        if self.pending_args:
            args, kwargs = self.pending_args
            self.callback(*args, **kwargs)
        self.timer = None
        self.pending_args = None

# Usage in app
class OptimizedApp(App):
    def compose(self):
        yield Input(placeholder="Type here...", id="search")

    def on_mount(self) -> None:
        """Initialize debouncer."""
        # Debounce search to avoid excessive updates
        self.debounced_search = Debouncer(0.5, self.perform_search)

    def on_input_changed(self, event: Input.Changed) -> None:
        """Handle input with debouncing."""
        if event.input.id == "search":
            # Only search after user stops typing
            self.debounced_search(event.value)

    def perform_search(self, query: str):
        """Perform search (only called when debounced)."""
        # Expensive search operation
        results = self.search(query)
        self.display_results(results)
```

### Throttling Events

```python
class Throttler:
    """Event throttler to limit event frequency."""

    def __init__(self, interval: float, callback):
        self.interval = interval
        self.callback = callback
        self.last_call = 0

    def __call__(self, *args, **kwargs):
        """Throttled function call."""
        import time
        now = time.time()

        if now - self.last_call >= self.interval:
            self.last_call = now
            self.callback(*args, **kwargs)

# Usage for mouse events
class MouseTracker(App):
    def compose(self):
        yield Static("Move mouse here", id="area")

    def on_mount(self) -> None:
        """Initialize throttler."""
        # Throttle mouse move to 10 per second
        self.mouse_throttler = Throttler(0.1, self.handle_mouse_move)

    def on_mouse_move(self, event) -> None:
        """Handle mouse with throttling."""
        if event.widget.id == "area":
            self.mouse_throttler(event.screen_x, event.screen_y)

    def handle_mouse_move(self, x: int, y: int):
        """Handle throttled mouse move."""
        # Only called max 10 times per second
        self.log(f"Mouse: {x}, {y}")
```

### Batch Event Processing

```python
class BatchProcessor:
    """Process events in batches."""

    def __init__(self, batch_size: int = 10, delay: float = 0.1):
        self.batch_size = batch_size
        self.delay = delay
        self.pending_events = []
        self.timer = None

    def add_event(self, event):
        """Add event to batch."""
        self.pending_events.append(event)

        # Process batch if full
        if len(self.pending_events) >= self.batch_size:
            self.process_batch()
        elif not self.timer:
            # Start timer for batch processing
            self.timer = self.set_timer(self.delay, self.process_batch)

    def process_batch(self):
        """Process all pending events."""
        if self.pending_events:
            batch = self.pending_events.copy()
            self.pending_events.clear()

            if self.timer:
                self.timer.stop()
                self.timer = None

            self.handle_batch(batch)

    def handle_batch(self, events):
        """Handle batch of events."""
        # Process multiple events together
        for event in events:
            self.process_event(event)

class EventBatchApp(App):
    """App with batch event processing."""

    def __init__(self):
        super().__init__()
        self.processor = BatchProcessor(batch_size=5)

    def compose(self):
        for i in range(20):
            yield Button(f"Button {i}", id=f"btn-{i}")

    def on_button_pressed(self, event: Button.Pressed) -> None:
        """Batch button press events."""
        self.processor.add_event(event)

    def process_event(self, event: Button.Pressed):
        """Process individual event."""
        self.log(f"Processed: {event.button.id}")
```

## Async Performance

### Async Operation Optimization

```python
import asyncio
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor

class AsyncOptimizer:
    """Optimize async operations."""

    def __init__(self, max_workers: int = 4):
        self.thread_pool = ThreadPoolExecutor(max_workers=max_workers)
        self.process_pool = ProcessPoolExecutor(max_workers=max_workers)

    async def run_cpu_bound(self, func, *args):
        """Run CPU-bound task in process pool."""
        loop = asyncio.get_event_loop()
        return await loop.run_in_executor(
            self.process_pool,
            func,
            *args
        )

    async def run_io_bound(self, func, *args):
        """Run I/O-bound task in thread pool."""
        loop = asyncio.get_event_loop()
        return await loop.run_in_executor(
            self.thread_pool,
            func,
            *args
        )

# Usage
class AsyncApp(App):
    def compose(self):
        yield Button("CPU Task", id="cpu")
        yield Button("IO Task", id="io")
        yield Static("", id="result")

    def on_mount(self) -> None:
        """Initialize optimizer."""
        self.optimizer = AsyncOptimizer(max_workers=4)

    async def on_button_pressed_cpu(self, event: Button.Pressed) -> None:
        """Run CPU-intensive task."""
        def cpu_task():
            # CPU-intensive calculation
            result = sum(i * i for i in range(1000000))
            return result

        result_widget = self.query_one("#result", Static)
        result_widget.update("Processing CPU task...")
        result = await self.optimizer.run_cpu_bound(cpu_task)
        result_widget.update(f"Result: {result}")

    async def on_button_pressed_io(self, event: Button.Pressed) -> None:
        """Run I/O-bound task."""
        async def io_task():
            # Simulate I/O
            await asyncio.sleep(1)
            return "I/O Complete"

        result_widget = self.query_one("#result", Static)
        result_widget.update("Processing I/O task...")
        result = await io_task()
        result_widget.update(result)
```

### Async Data Loading

```python
class AsyncDataLoader:
    """Efficient async data loader."""

    def __init__(self, page_size: int = 100):
        self.page_size = page_size
        self.cache = {}
        self.loading_pages = set()

    async def get_page(self, page_num: int):
        """Get data page asynchronously."""
        if page_num in self.cache:
            return self.cache[page_num]

        if page_num in self.loading_pages:
            # Already loading, wait for it
            await self.wait_for_page(page_num)
            return self.cache[page_num]

        self.loading_pages.add(page_num)

        try:
            # Fetch page
            page_data = await self.fetch_page(page_num)
            self.cache[page_num] = page_data
            return page_data
        finally:
            self.loading_pages.discard(page_num)

    async def fetch_page(self, page_num: int):
        """Fetch page from source."""
        # Simulate async fetch
        await asyncio.sleep(0.1)
        start = page_num * self.page_size
        end = start + self.page_size
        return [{"id": i, "data": f"Item {i}"} for i in range(start, end)]

    async def prefetch_pages(self, pages: list):
        """Prefetch multiple pages."""
        tasks = [self.get_page(page) for page in pages]
        await asyncio.gather(*tasks)

class PagedView(App):
    """Virtualized paged view."""

    def __init__(self):
        super().__init__()
        self.loader = AsyncDataLoader(page_size=50)
        self.current_page = 0
        self.visible_pages = 3  # Show 3 pages

    def compose(self):
        yield Button("Previous", id="prev")
        yield Button("Next", id="next")
        yield Static("", id="page-info")
        yield Static("", id="data")

    async def on_mount(self) -> None:
        """Load initial page."""
        await self.load_current_page()

    async def load_current_page(self):
        """Load current page."""
        data = await self.loader.get_page(self.current_page)
        self.display_data(data)
        self.update_page_info()

    def display_data(self, data):
        """Display page data."""
        display = self.query_one("#data", Static)
        display.update("\n".join(item["data"] for item in data))

    def update_page_info(self):
        """Update page info display."""
        info = self.query_one("#page-info", Static)
        info.update(f"Page {self.current_page}")

    async def on_button_pressed_next(self, event: Button.Pressed) -> None:
        """Go to next page."""
        self.current_page += 1
        await self.load_current_page()

        # Prefetch next pages
        next_pages = [self.current_page + i for i in range(1, self.visible_pages)]
        await self.loader.prefetch_pages(next_pages)

    async def on_button_pressed_prev(self, event: Button.Pressed) -> None:
        """Go to previous page."""
        if self.current_page > 0:
            self.current_page -= 1
            await self.load_current_page()
```

## Memory Optimization

### Widget Pooling

```python
class WidgetPool:
    """Pool of reusable widgets."""

    def __init__(self, widget_class, *args, **kwargs):
        self.widget_class = widget_class
        self.pool = []
        self.in_use = set()

    def get(self, *args, **kwargs):
        """Get widget from pool."""
        if self.pool:
            widget = self.pool.pop()
            # Reinitialize if needed
            return widget
        else:
            # Create new widget
            widget = self.widget_class(*args, **kwargs)
            self.in_use.add(widget)
            return widget

    def return_(self, widget):
        """Return widget to pool."""
        if widget in self.in_use:
            self.in_use.remove(widget)
            # Reset widget state
            self.pool.append(widget)

class ListView(App):
    """Efficient list view with widget pooling."""

    def __init__(self):
        super().__init__()
        self.item_pool = WidgetPool(Static)
        self.visible_items = 20  # Show only 20 items
        self.all_items = []

    def compose(self):
        yield Static("", id="list-container")

    def set_items(self, items):
        """Set items efficiently."""
        self.all_items = items
        self.render_visible_items()

    def render_visible_items(self):
        """Render only visible items."""
        container = self.query_one("#list-container", Static)

        # Get subset of items
        subset = self.all_items[:self.visible_items]

        # Format items
        formatted = "\n".join(str(item) for item in subset)
        container.update(formatted)
```

### Garbage Collection Hints

```python
class GCOptimizedApp(App):
    """App with garbage collection optimization."""

    def __init__(self):
        super().__init__()
        self._large_data = None

    def set_large_data(self, data):
        """Set large data with cleanup of old data."""
        # Clear reference to old data
        self._large_data = None
        import gc
        gc.collect()  # Force GC

        # Set new data
        self._large_data = data

    def cleanup_old_widgets(self):
        """Clean up unused widgets."""
        # Remove widgets from DOM
        for widget in self.query(".old-data").results():
            widget.remove()

        import gc
        gc.collect()

    def on_unmount(self) -> None:
        """Clean up on unmount."""
        # Clear large references
        self._large_data = None
        self.clear_widgets()
        import gc
        gc.collect()

        super().on_unmount()
```

## Profiling Tools

### Built-in Profiler

```python
from textual.app import App
import cProfile
import io
import pstats

class ProfiledApp(App):
    """App with built-in profiling."""

    def on_mount(self) -> None:
        """Start profiling."""
        self.profiler = cProfile.Profile()
        self.profiler.enable()

    def on_unmount(self) -> None:
        """Stop profiling and print results."""
        self.profiler.disable()

        # Get results
        s = io.StringIO()
        stats = pstats.Stats(self.profiler, stream=s)
        stats.sort_stats('cumulative')
        stats.print_stats(20)  # Top 20 functions

        # Save to file
        with open('profile_stats.txt', 'w') as f:
            f.write(s.getvalue())

        super().on_unmount()
```

### Custom Performance Monitor

```python
class PerformanceTracker:
    """Track app performance metrics."""

    def __init__(self):
        self.metrics = {
            "renders": [],
            "events": [],
            "updates": [],
        }

    def start_timer(self):
        """Start timing operation."""
        return TimerContext(self)

    def add_metric(self, category: str, duration: float):
        """Add performance metric."""
        self.metrics[category].append(duration)

    def get_report(self) -> str:
        """Get performance report."""
        report = ["Performance Report", "=" * 50]

        for category, values in self.metrics.items():
            if values:
                avg = sum(values) / len(values)
                max_time = max(values)
                min_time = min(values)
                report.append(f"\n{category.upper()}:")
                report.append(f"  Count: {len(values)}")
                report.append(f"  Avg: {avg:.3f}s")
                report.append(f"  Max: {max_time:.3f}s")
                report.append(f"  Min: {min_time:.3f}s")

        return "\n".join(report)

class TimerContext:
    """Context manager for timing."""

    def __init__(self, tracker, category: str):
        self.tracker = tracker
        self.category = category
        self.start_time = None

    def __enter__(self):
        import time
        self.start_time = time.time()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        import time
        duration = time.time() - self.start_time
        self.tracker.add_metric(self.category, duration)

# Usage
class MonitoredApp(App):
    def compose(self):
        yield Button("Test", id="test")

    def on_mount(self) -> None:
        """Initialize tracker."""
        self.tracker = PerformanceTracker()

    def on_button_pressed_test(self, event: Button.Pressed) -> None:
        """Test with performance tracking."""
        with self.tracker.start_timer() as timer:
            # Perform operation
            self.heavy_operation()

    def heavy_operation(self):
        """Simulate heavy operation."""
        import time
        time.sleep(0.1)
```

## Performance Testing

### Load Testing

```python
import asyncio
import time

class LoadTestApp(App):
    """App for load testing."""

    def compose(self):
        for i in range(100):
            yield Button(f"Button {i}", id=f"btn-{i}")

    def on_button_pressed(self, event: Button.Pressed) -> None:
        """Handle button press."""
        # Simulate work
        time.sleep(0.001)

async def test_button_presses():
    """Test multiple button presses."""
    app = LoadTestApp()

    async with app.run_test() as pilot:
        # Measure time for 100 button clicks
        start = time.time()

        for i in range(100):
            await pilot.click(f"#btn-{i}")

        duration = time.time() - start

        # Should handle 100 clicks in reasonable time
        assert duration < 10.0, f"Too slow: {duration}s"

        print(f"100 button presses took {duration:.3f}s")
```

### Memory Usage Testing

```python
import psutil
import os

class MemoryTestApp(App):
    """App for memory testing."""

    def __init__(self):
        super().__init__()
        self.large_data = []

    def compose(self):
        yield Button("Load Data", id="load")
        yield Button("Clear Data", id="clear")

    def on_button_pressed_load(self, event: Button.Pressed) -> None:
        """Load large amount of data."""
        self.large_data = [{"id": i, "data": "x" * 1000} for i in range(1000)]

    def on_button_pressed_clear(self, event: Button.Pressed) -> None:
        """Clear data."""
        self.large_data.clear()

def get_memory_usage():
    """Get current memory usage in MB."""
    process = psutil.Process(os.getpid())
    return process.memory_info().rss / 1024 / 1024

async def test_memory_usage():
    """Test memory usage."""
    initial_memory = get_memory_usage()

    app = MemoryTestApp()
    async with app.run_test() as pilot:
        # Load data
        await pilot.click("#load")
        after_load = get_memory_usage()

        # Clear data
        await pilot.click("#clear")
        after_clear = get_memory_usage()

        print(f"Initial: {initial_memory:.1f} MB")
        print(f"After load: {after_load:.1f} MB")
        print(f"After clear: {after_clear:.1f} MB")

        # Memory should be released after clear
        assert (after_clear - initial_memory) < 10.0, "Memory not released"
```

## Best Practices

### 1. Minimize Widget Count

```python
# Good: Use containers to group widgets
with Vertical():
    for item in items:
        yield Static(item)  # Few widgets

# Avoid: Individual widgets for each item
for item in items:
    with Horizontal():
        yield Static(item)  # Many nested widgets
```

### 2. Use Efficient Data Structures

```python
# Good: Dict for lookups
data = {id: item for id, item in items}
item = data[id]  # O(1)

# Avoid: List for lookups
data = items
item = next(i for i in data if i.id == id)  # O(n)
```

### 3. Batch DOM Updates

```python
# Good: Batch updates
def update_display(self, items):
    with self.batch():
        for item in self.query('.item').results():
            item.update(items.pop(0))

# Avoid: Individual updates
def update_display(self, items):
    for item in self.query('.item').results():
        item.update(items.pop(0))
```

### 4. Cache Expensive Operations

```python
# Good: Cache results
@cache.memoize(maxsize=128)
def expensive_calculation(self, value):
    # Expensive operation
    return result

# Avoid: Recalculate every time
def expensive_calculation(self, value):
    # Expensive operation
    return result
```

### 5. Use Async for I/O

```python
# Good: Async I/O
async def fetch_data(self):
    return await self.api_client.get('/data')

# Avoid: Blocking I/O
def fetch_data(self):
    return requests.get('/data').json()
```

### 6. Optimize Event Handlers

```python
# Good: Efficient event handling
def on_button_pressed(self, event: Button.Pressed) -> None:
    # Minimal work in event handler
    self.schedule_update(event.button.id)

def schedule_update(self, button_id):
    # Actual work deferred
    self.call_later(self.do_update, button_id)

# Avoid: Heavy work in event handler
def on_button_pressed(self, event: Button.Pressed) -> None:
    # Heavy work blocks UI
    result = self.heavy_calculation()
    self.update_ui(result)
```

### 7. Use Appropriate Refresh Methods

```python
# Use refresh() for minor changes
widget.refresh()  # Partial refresh

# Use update() for content changes
widget.update("New content")  # Full update

# Use remove()/mount() for structural changes
old_widget.remove()
new_widget.mount()  # Structural change
```

### 8. Monitor Performance

```python
# Good: Regular performance monitoring
def on_mount(self) -> None:
    self.set_interval(5.0, self.check_performance)

def check_performance(self):
    """Monitor and log performance issues."""
    stats = self.get_performance_stats()
    if stats.render_time > 0.1:
        self.log(f"Slow renders: {stats.render_time:.3f}s")

# Always monitor in production
```

## Performance Checklist

### Before Development
- [ ] Design efficient data structures
- [ ] Plan caching strategy
- [ ] Identify performance bottlenecks
- [ ] Set performance targets

### During Development
- [ ] Profile hot paths
- [ ] Minimize widget count
- [ ] Batch DOM updates
- [ ] Use appropriate event handling
- [ ] Implement lazy loading where needed
- [ ] Cache expensive operations

### Testing
- [ ] Load testing with expected data sizes
- [ ] Memory usage testing
- [ ] Performance regression tests
- [ ] Profile critical paths

### Production
- [ ] Monitor performance metrics
- [ ] Log slow operations
- [ ] Track memory usage
- [ ] Profile production workloads

## See Also

- [Textual Testing Utilities](textual-testing-utilities.md)
- [Textual Events Handling](textual-events-handling.md)
- [Textual Data Binding](textual-data-binding.md)
- [Textual Widgets Reference](textual-widgets-reference.md)
