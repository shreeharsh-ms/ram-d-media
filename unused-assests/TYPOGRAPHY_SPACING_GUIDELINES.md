# 🎨 EDEN Digital Media - Typography & Spacing Guidelines

**Document Version**: 1.0  
**Date**: April 2, 2026  
**Project**: Complete Typography & Spacing Standardization  
**Status**: Active Implementation Guide  

---

## 📋 Executive Summary

This document establishes comprehensive guidelines for typography (font families, font sizes, font weights) and spacing (padding, margins, gaps) across the EDEN Digital Media website. These standards ensure visual consistency, readability, and professional brand presentation.

**Key Principles**:
- ✅ Strict font family standardization (only 3 approved fonts)
- ✅ Hierarchical text sizing system using CSS `clamp()`
- ✅ Consistent padding and margin scale
- ✅ Professional spacing ratios
- ✅ Accessible text sizing (WCAG compliant)

---

## 🔤 Part 1: Font Family Standardization

### Approved Font Families (ONLY THESE THREE)

#### 1. **Primary Heading Font** - Playfair Display
- **Purpose**: Large headlines, section titles, hero text
- **Google Fonts Import**: 
  ```html
  <link href="https://fonts.googleapis.com/css2?family=Playfair+Display:wght@400;700&display=swap" rel="stylesheet">
  ```
- **CSS Usage**: `font-family: 'Playfair Display', serif;`
- **Available Weights**: 400 (regular), 700 (bold)
- **Character Set**: Latin (covers all English text)
- **Use Cases**:
  - Page titles (h1, h2)
  - Section headings
  - Hero content
  - Featured quotes
  - Brand statements

**Example CSS**:
```css
h1, h2, .main-heading, .hero-content h1 {
    font-family: 'Playfair Display', serif;
    font-weight: 700;
}
```

---

#### 2. **Body & UI Font** - Inter
- **Purpose**: Body text, labels, buttons, navigation, all UI elements
- **Google Fonts Import**: 
  ```html
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;700&display=swap" rel="stylesheet">
  ```
- **CSS Usage**: `font-family: 'Inter', sans-serif;`
- **Available Weights**: 300 (light), 400 (regular), 600 (semi-bold), 700 (bold)
- **Character Set**: Latin (covers all English text)
- **Use Cases**:
  - Paragraph text
  - Navigation links
  - Button text
  - Form labels and inputs
  - Card descriptions
  - Metadata and timestamps
  - Badges and tags

**Example CSS**:
```css
body, p, a, button, input, label, span {
    font-family: 'Inter', sans-serif;
}
```

---

#### 3. **Decorative/Script Font** - Great Vibes
- **Purpose**: Accent, decorative, brand sub-text
- **Google Fonts Import**: 
  ```html
  <link href="https://fonts.googleapis.com/css2?family=Great+Vibes&display=swap" rel="stylesheet">
  ```
- **CSS Usage**: `font-family: 'Great Vibes', cursive;`
- **Available Weights**: 400 (regular) only
- **Character Set**: Latin (covers all English text)
- **Use Cases**:
  - Logo subtitle (e.g., "Digital Media" under EDEN)
  - Taglines
  - Accent decorative text
  - Special emphasis on limited text only

**Example CSS**:
```css
.logo-sub, .brand-tagline, .decorative-text {
    font-family: 'Great Vibes', cursive;
    font-weight: 400;
}
```

---

#### 4. **Uppercase Display Font** - Oswald (Optional/Limited)
- **Purpose**: Uppercase titles, vertical text
- **Google Fonts Import**: 
  ```html
  <link href="https://fonts.googleapis.com/css2?family=Oswald:wght@700&display=swap" rel="stylesheet">
  ```
- **CSS Usage**: `font-family: 'Oswald', sans-serif;`
- **Available Weights**: 700 (bold) only
- **Character Set**: Latin (covers all English text)
- **Use Cases**:
  - Vertical section titles
  - All-caps headings only
  - Very limited decorative use

**Example CSS**:
```css
.work-title {
    font-family: 'Oswald', sans-serif;
    font-weight: 700;
    text-transform: uppercase;
}
```

---

### Font Family Rules (STRICT)

| Element | Font Family | Weight | Color | Rule |
|---------|-------------|--------|-------|------|
| `h1` | Playfair Display | 700 | Primary | **REQUIRED** - Headlines only |
| `h2` | Playfair Display | 700 | Primary | **REQUIRED** - Section titles |
| `h3, h4, h5, h6` | Inter | 700 | Primary | Default for smaller headings |
| `p, body, span` | Inter | 400 | Primary | **MANDATORY** - Body text |
| `a` (links) | Inter | 600 | Accent | Links must be Inter |
| `button` | Inter | 600 | Varies | Buttons must be Inter |
| `input, label` | Inter | 400 | Text | Forms must be Inter |
| `.nav-link` | Inter | 500 | Text | Navigation must be Inter |
| `.logo-sub` | Great Vibes | 400 | Accent | ONLY for logo subtitle |
| `.work-title` | Oswald | 700 | Text | ONLY for vertical titles |

---

### Font Fallback Stack (if web fonts fail)
```css
:root {
    --font-display: 'Playfair Display', 'Georgia', 'Times New Roman', serif;
    --font-body: 'Inter', 'Segoe UI', 'Roboto', 'Oxygen', 'Ubuntu', sans-serif;
    --font-script: 'Great Vibes', 'Brush Script MT', cursive;
    --font-oswald: 'Oswald', 'Arial', sans-serif;
}
```

---

## 📏 Part 2: Font Size System

### Responsive Font Sizing with CSS `clamp()`

The `clamp()` function creates fluid, responsive font sizes that scale smoothly between mobile and desktop.

**Syntax**: `font-size: clamp(mobile_size, viewport_size, desktop_size);`

---

### Font Size Scale (Hierarchical)

#### **Level 1: Extra Large Headings** (Hero Text)
```css
font-size: clamp(2.5rem, 6vw, 5rem);
```
- **Mobile (375px)**: ~2.5rem (40px)
- **Tablet (768px)**: ~3.5rem (56px)
- **Desktop (1920px)**: ~5rem (80px)
- **Use Cases**: h1, main hero heading, large section titles
- **Font Family**: Playfair Display
- **Font Weight**: 700
- **Line Height**: 1.1

---

#### **Level 2: Large Headings**
```css
font-size: clamp(2rem, 4.5vw, 4.5rem);
```
- **Mobile (375px)**: ~2rem (32px)
- **Tablet (768px)**: ~2.8rem (45px)
- **Desktop (1920px)**: ~4.5rem (72px)
- **Use Cases**: h2, section titles, card titles
- **Font Family**: Playfair Display or Inter (bold)
- **Font Weight**: 700
- **Line Height**: 1.2

---

#### **Level 3: Medium Headings**
```css
font-size: clamp(1.5rem, 3vw, 3rem);
```
- **Mobile (375px)**: ~1.5rem (24px)
- **Tablet (768px)**: ~2rem (32px)
- **Desktop (1920px)**: ~3rem (48px)
- **Use Cases**: h3, card headings, feature titles
- **Font Family**: Playfair Display or Inter
- **Font Weight**: 600-700
- **Line Height**: 1.3

---

#### **Level 4: Small Headings**
```css
font-size: clamp(1.2rem, 2vw, 2rem);
```
- **Mobile (375px)**: ~1.2rem (19px)
- **Tablet (768px)**: ~1.5rem (24px)
- **Desktop (1920px)**: ~2rem (32px)
- **Use Cases**: h4, subsections, feature names
- **Font Family**: Inter
- **Font Weight**: 600-700
- **Line Height**: 1.4

---

#### **Level 5: Body Text (Large)**
```css
font-size: clamp(1.05rem, 1.5vw, 1.25rem);
```
- **Mobile (375px)**: ~1.05rem (17px)
- **Tablet (768px)**: ~1.13rem (18px)
- **Desktop (1920px)**: ~1.25rem (20px)
- **Use Cases**: Large paragraph text, introductions
- **Font Family**: Inter
- **Font Weight**: 400
- **Line Height**: 1.6

---

#### **Level 6: Body Text (Regular)**
```css
font-size: clamp(0.95rem, 1.2vw, 1.1rem);
```
- **Mobile (375px)**: ~0.95rem (15px)
- **Tablet (768px)**: ~1.02rem (16px)
- **Desktop (1920px)**: ~1.1rem (18px)
- **Use Cases**: Standard paragraph text
- **Font Family**: Inter
- **Font Weight**: 400
- **Line Height**: 1.6-1.7

---

#### **Level 7: Body Text (Small)**
```css
font-size: clamp(0.9rem, 1vw, 1rem);
```
- **Mobile (375px)**: ~0.9rem (14px)
- **Tablet (768px)**: ~0.96rem (15px)
- **Desktop (1920px)**: ~1rem (16px)
- **Use Cases**: Metadata, descriptions, secondary text
- **Font Family**: Inter
- **Font Weight**: 400
- **Line Height**: 1.5-1.6

---

#### **Level 8: UI Text (Labels, Tags)**
```css
font-size: clamp(0.8rem, 0.9vw, 0.95rem);
```
- **Mobile (375px)**: ~0.8rem (13px)
- **Tablet (768px)**: ~0.88rem (14px)
- **Desktop (1920px)**: ~0.95rem (15px)
- **Use Cases**: Form labels, tags, badges, navigation
- **Font Family**: Inter
- **Font Weight**: 500-600
- **Line Height**: 1.4

---

#### **Level 9: Small UI Text (Captions)**
```css
font-size: clamp(0.7rem, 0.8vw, 0.85rem);
```
- **Mobile (375px)**: ~0.7rem (11px)
- **Tablet (768px)**: ~0.78rem (12px)
- **Desktop (1920px)**: ~0.85rem (14px)
- **Use Cases**: Captions, timestamps, fine print
- **Font Family**: Inter
- **Font Weight**: 400
- **Line Height**: 1.3-1.4

---

### Font Size Reference Table

| Level | Mobile | Tablet | Desktop | Usage | Font |
|-------|--------|--------|---------|-------|------|
| 1 | 2.5rem | 3.5rem | 5rem | Hero h1 | Playfair |
| 2 | 2rem | 2.8rem | 4.5rem | Section h2 | Playfair |
| 3 | 1.5rem | 2rem | 3rem | Card h3 | Playfair/Inter |
| 4 | 1.2rem | 1.5rem | 2rem | Heading h4 | Inter |
| 5 | 1.05rem | 1.13rem | 1.25rem | Large Body | Inter |
| 6 | 0.95rem | 1.02rem | 1.1rem | Body Text | Inter |
| 7 | 0.9rem | 0.96rem | 1rem | Small Body | Inter |
| 8 | 0.8rem | 0.88rem | 0.95rem | Labels | Inter |
| 9 | 0.7rem | 0.78rem | 0.85rem | Captions | Inter |

---

### Line Height Standards

| Text Type | Line Height | Reason |
|-----------|-------------|--------|
| Headings (h1-h4) | 1.1 - 1.3 | Tight for visual impact |
| Large Body (1.2rem+) | 1.6 - 1.7 | Readable, airy |
| Standard Body | 1.6 - 1.7 | WCAG AA recommendation |
| Small Text | 1.4 - 1.5 | Compact but readable |
| UI Text/Labels | 1.4 - 1.5 | Tight, compact |
| Links | 1.6 | Same as body text |

---

### Letter Spacing Standards

| Text Type | Letter Spacing | Use Cases |
|-----------|----------------|-----------|
| Headings (Playfair) | -5px to -2px | Large text, visual tightness |
| Headings (Inter) | 0 (normal) | Standard headings |
| Navigation | 0.5px - 1px | Small caps, uppercase |
| Labels/Tags | 1px - 1.5px | Uppercase labels |
| Body Text | 0 (normal) | Paragraph text |
| CTA Text | 0.5px | Button text, slight separation |

---

## 📐 Part 3: Padding & Margin System

### Spacing Scale (8px Base)

The spacing system uses an 8px base unit, creating consistent multiples:

| Scale | Value | Usage |
|-------|-------|-------|
| xs | 4px | Tiny gaps, borders |
| sm | 8px | Small spacing, inline |
| md | 16px | Default spacing, padding |
| lg | 24px | Large padding, section spacing |
| xl | 32px | Extra large, section gaps |
| 2xl | 40px | Major spacing |
| 3xl | 48px | Large section separation |
| 4xl | 56px | Extra large gaps |
| 5xl | 64px | Hero sections |
| 6xl | 80px | Maximum spacing |

---

### CSS Variables for Spacing

```css
:root {
    /* Spacing Scale (8px base) */
    --spacing-xs: 4px;
    --spacing-sm: 8px;
    --spacing-md: 16px;
    --spacing-lg: 24px;
    --spacing-xl: 32px;
    --spacing-2xl: 40px;
    --spacing-3xl: 48px;
    --spacing-4xl: 56px;
    --spacing-5xl: 64px;
    --spacing-6xl: 80px;
    --spacing-7xl: 100px;
    
    /* Responsive Padding */
    --section-padding: clamp(40px, 8vw, 100px);
    --card-padding: clamp(20px, 3vw, 40px);
    --element-padding: clamp(12px, 2vw, 24px);
}
```

---

### Padding Standards by Component

#### **Section Padding**
```css
section {
    padding: clamp(60px, 10vw, 120px) clamp(40px, 5vw, 80px);
}
```
- **Mobile (375px)**: 60px vertical, 40px horizontal
- **Tablet (768px)**: ~85px vertical, ~60px horizontal
- **Desktop (1920px)**: 120px vertical, 80px horizontal

---

#### **Container Padding**
```css
.container {
    padding: 0 clamp(20px, 5vw, 80px);
}
```
- **Mobile**: 20px left/right
- **Tablet**: ~50px left/right
- **Desktop**: 80px left/right

---

#### **Card Padding**
```css
.card {
    padding: clamp(20px, 3vw, 40px);
}
```
- **Mobile**: 20px
- **Tablet**: ~30px
- **Desktop**: 40px

---

#### **Button Padding**
```css
.btn {
    padding: 14px 32px;  /* Fixed - not responsive */
    border-radius: 40px;
}
```
- **Vertical**: 14px (fixed)
- **Horizontal**: 32px (fixed)
- **Ensures**: Consistent clickable area

---

#### **Form Input Padding**
```css
input, textarea {
    padding: 12px 16px;
}
```
- **Vertical**: 12px
- **Horizontal**: 16px
- **Height**: ~44-48px (touch-friendly)

---

#### **Navigation Padding**
```css
nav {
    padding: 20px 0;
}

.nav-link {
    padding: 8px 12px;
}
```
- **Navigation bar**: 20px vertical
- **Link**: 8px vertical, 12px horizontal

---

#### **Hero Section Padding**
```css
.hero {
    padding-top: clamp(100px, 15vw, 200px);
    padding: 0 clamp(40px, 8vw, 80px);
    gap: clamp(20px, 3vw, 40px);
}
```
- **Top**: 100-200px (below navbar)
- **Sides**: 40-80px
- **Gap between columns**: 20-40px

---

### Margin Standards by Component

#### **Section Margin**
```css
section {
    margin-bottom: clamp(60px, 10vw, 100px);
}
```

---

#### **Text Margin**
```css
h1, h2, h3 {
    margin-bottom: clamp(16px, 2vw, 32px);
}

p {
    margin-bottom: clamp(16px, 2vw, 24px);
}
```

---

#### **Heading to Text Margin**
```css
h1 + p {
    margin-top: -8px;  /* Optical adjustment */
    margin-bottom: clamp(24px, 3vw, 40px);
}
```

---

#### **List Item Margin**
```css
li {
    margin-bottom: 8px;
}
```

---

### Gap Standards (Flexbox/Grid)

| Component | Gap Value | Usage |
|-----------|-----------|-------|
| Navigation | 40px | Between nav links |
| Button Group | 12px | Between buttons |
| Card Grid | 24px | Between cards |
| Flex Row | 16px | General flex gap |
| Flex Column | 20px | Vertical flex gap |
| List Items | 8px | Between list items |
| Form Fields | 16px | Between inputs |

---

## 📐 Part 4: Component-Specific Guidelines

### Hero Section

```css
.hero {
    padding: clamp(100px, 15vw, 150px) clamp(40px, 8vw, 80px);
    gap: clamp(20px, 3vw, 40px);
}

.hero-content h1 {
    font-family: 'Playfair Display', serif;
    font-size: clamp(2.5rem, 5vw, 4.5rem);
    font-weight: 700;
    line-height: 1.1;
    margin-bottom: 20px;
    letter-spacing: -5px;
}

.hero-content h4 {
    font-family: 'Inter', sans-serif;
    font-size: clamp(0.8rem, 1vw, 0.95rem);
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 2px;
    margin-bottom: 25px;
}

.hero-content p {
    font-family: 'Inter', sans-serif;
    font-size: clamp(0.95rem, 1.2vw, 1.1rem);
    font-weight: 400;
    line-height: 1.7;
    margin-bottom: 35px;
    max-width: 380px;
}

.stat-box {
    padding: 30px;
    margin-bottom: 15px;
}

.stat-num {
    font-family: 'Inter', sans-serif;
    font-size: clamp(1.8rem, 3vw, 2.2rem);
    font-weight: 600;
}

.stat-txt {
    font-family: 'Inter', sans-serif;
    font-size: 11px;
    font-weight: 700;
    letter-spacing: 1.5px;
    margin-top: 8px;
}
```

---

### Navigation Bar

```css
header {
    padding: 20px 0;
}

.nav-group {
    gap: 60px;
}

.nav-link {
    font-family: 'Inter', sans-serif;
    font-size: 18px;
    font-weight: 500;
    padding: 8px 12px;
    letter-spacing: 0px;
}

.logo-main {
    font-family: 'Playfair Display', serif;
    font-size: 42px;
    font-weight: 700;
    letter-spacing: 2px;
}

.logo-sub {
    font-family: 'Great Vibes', cursive;
    font-size: 38px;
    font-weight: 400;
    margin-top: -5px;
}
```

---

### Cards

```css
.card {
    padding: clamp(20px, 3vw, 40px);
    border-radius: 24px;
}

.card h3 {
    font-family: 'Playfair Display', serif;
    font-size: clamp(1.5rem, 3vw, 2.5rem);
    font-weight: 700;
    margin-bottom: 15px;
    line-height: 1.2;
}

.card p {
    font-family: 'Inter', sans-serif;
    font-size: clamp(0.9rem, 1vw, 1.05rem);
    font-weight: 400;
    line-height: 1.6;
    margin-bottom: 20px;
}
```

---

### Buttons

```css
.btn {
    font-family: 'Inter', sans-serif;
    font-size: 13px;
    font-weight: 600;
    padding: 14px 32px;
    border-radius: 40px;
    letter-spacing: 0.5px;
}

.btn-large {
    font-size: 15px;
    padding: 18px 45px;
    letter-spacing: 1px;
}

.btn-small {
    font-size: 11px;
    padding: 10px 20px;
    letter-spacing: 0px;
}
```

---

### Forms

```css
input, textarea {
    font-family: 'Inter', sans-serif;
    font-size: 14px;
    font-weight: 400;
    padding: 12px 16px;
    line-height: 1.5;
}

label {
    font-family: 'Inter', sans-serif;
    font-size: clamp(0.8rem, 0.9vw, 0.95rem);
    font-weight: 600;
    margin-bottom: 8px;
    display: block;
    letter-spacing: 0px;
}

::placeholder {
    font-family: 'Inter', sans-serif;
    font-size: 14px;
    font-weight: 400;
    letter-spacing: 0px;
}
```

---

### Footer

```css
.footer-top p {
    font-family: 'Inter', sans-serif;
    font-size: 14px;
    font-weight: 700;
    margin-bottom: 10px;
    letter-spacing: 0px;
}

.main-heading {
    font-family: 'Playfair Display', serif;
    font-size: clamp(4rem, 15vw, 12rem);
    font-weight: 800;
    letter-spacing: -5px;
    line-height: 0.9;
    margin-bottom: 80px;
}

.grid-column h4 {
    font-family: 'Inter', sans-serif;
    font-size: 11px;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 1px;
    margin-bottom: 25px;
}

.grid-column ul li {
    font-family: 'Inter', sans-serif;
    font-size: 14px;
    font-weight: 400;
    margin-bottom: 8px;
    line-height: 1.5;
}

.brand h2 {
    font-family: 'Playfair Display', serif;
    font-size: 32px;
    font-weight: 800;
    line-height: 1;
}

.local-time h4 {
    font-family: 'Inter', sans-serif;
    font-size: 11px;
    font-weight: 700;
    text-transform: uppercase;
}

.local-time p {
    font-family: 'Inter', sans-serif;
    font-size: 14px;
    font-weight: 400;
}
```

---

## 🔍 Part 5: Typography Hierarchy Rules

### When to Use Each Font

#### **Playfair Display** (Serif)
```
✅ DO USE:
  - Main page headings (h1, h2)
  - Section titles
  - Hero content
  - Large branded text
  - Quotes or testimonials
  
❌ DON'T USE:
  - Body paragraphs
  - Navigation
  - Button text
  - Form labels
  - UI elements
```

#### **Inter** (Sans-serif)
```
✅ DO USE:
  - All body text
  - Navigation
  - Buttons
  - Form elements
  - Card descriptions
  - Labels and tags
  - Metadata
  
❌ DON'T USE:
  - Main headings (use Playfair)
  - Script/decorative purposes (use Great Vibes)
```

#### **Great Vibes** (Script)
```
✅ DO USE:
  - Logo subtitle only
  - Special accent text (very limited)
  - Taglines (maximum 1-2 per page)
  
❌ DON'T USE:
  - Body text
  - Navigation
  - Headings
  - Large blocks of text
  - Any formal content
```

#### **Oswald** (Display)
```
✅ DO USE:
  - Vertical titles only
  - All-caps headings (limited)
  - Special decorative elements
  
❌ DON'T USE:
  - Regular headings
  - Body text
  - Navigation
```

---

## 📝 Part 6: Font Weight Rules

### Standard Font Weights

| Font | Weight | Name | Usage |
|------|--------|------|-------|
| Playfair | 400 | Regular | Rarely used |
| Playfair | 700 | Bold | Headings (h1, h2) |
| Inter | 300 | Light | Not recommended |
| Inter | 400 | Regular | Body text, labels |
| Inter | 600 | Semi-Bold | Links, subheadings |
| Inter | 700 | Bold | Strong emphasis, tags |

---

### Font Weight Hierarchy

```
Heading (h1): 700 (Bold)
    ↓
Subheading (h2): 700 (Bold)
    ↓
Label/Small Heading (h4): 600-700 (Semi-bold or Bold)
    ↓
Body Text: 400 (Regular)
    ↓
UI Text/Navigation: 500-600 (Medium or Semi-bold)
```

---

## 📱 Part 7: Responsive Breakpoints

### Desktop (1024px+)
- Full padding: 80px+ sides
- Large font sizes (5rem+ for h1)
- All decorative fonts applied
- Maximum spacing gaps

### Tablet (768px - 1024px)
- Medium padding: 40-60px sides
- Medium font sizes (3-4rem for h1)
- Slightly reduced letter spacing
- Adjusted gaps

### Mobile (Below 768px)
- Reduced padding: 20-40px sides
- Small font sizes (2-2.5rem for h1)
- Tighter line heights
- Reduced gaps

---

## ✅ Part 8: Validation Checklist

### Font Family Audit
- [ ] All h1, h2 use Playfair Display
- [ ] All body text uses Inter
- [ ] Navigation uses Inter only
- [ ] Buttons use Inter only
- [ ] Logo subtitle uses Great Vibes
- [ ] Forms use Inter only
- [ ] No other fonts imported or used

### Font Size Audit
- [ ] All heading sizes use `clamp()`
- [ ] Heading hierarchy is clear
- [ ] Mobile sizes are readable (14px+)
- [ ] Desktop sizes are proportional
- [ ] Tablet transition is smooth

### Padding Audit
- [ ] All sections use consistent padding
- [ ] Cards have uniform padding
- [ ] Buttons have consistent padding
- [ ] Forms have proper spacing
- [ ] No random padding values

### Line Height Audit
- [ ] Headings: 1.1-1.3
- [ ] Body text: 1.6-1.7
- [ ] Small text: 1.4-1.5
- [ ] Good readability on all devices

### Letter Spacing Audit
- [ ] Large headings: -5px to -2px
- [ ] Navigation: 0-1px
- [ ] Labels: 1-1.5px
- [ ] Body text: 0 (normal)

---

## 🎯 Part 9: CSS Implementation Template

```css
:root {
    /* Font Families */
    --font-display: 'Playfair Display', serif;
    --font-body: 'Inter', sans-serif;
    --font-script: 'Great Vibes', cursive;
    --font-oswald: 'Oswald', sans-serif;
    
    /* Spacing Scale */
    --spacing-xs: 4px;
    --spacing-sm: 8px;
    --spacing-md: 16px;
    --spacing-lg: 24px;
    --spacing-xl: 32px;
    --spacing-2xl: 40px;
    --spacing-3xl: 48px;
    --spacing-4xl: 56px;
    --spacing-5xl: 64px;
    --spacing-6xl: 80px;
    
    /* Responsive Padding */
    --section-padding: clamp(60px, 10vw, 120px);
    --section-padding-h: clamp(40px, 5vw, 80px);
    --card-padding: clamp(20px, 3vw, 40px);
}

/* HEADINGS */
h1 {
    font-family: var(--font-display);
    font-size: clamp(2.5rem, 5vw, 4.5rem);
    font-weight: 700;
    line-height: 1.1;
    letter-spacing: -5px;
    margin-bottom: clamp(16px, 2vw, 32px);
}

h2 {
    font-family: var(--font-display);
    font-size: clamp(2rem, 4.5vw, 3.5rem);
    font-weight: 700;
    line-height: 1.2;
    letter-spacing: -2px;
    margin-bottom: clamp(16px, 2vw, 32px);
}

h3 {
    font-family: var(--font-display);
    font-size: clamp(1.5rem, 3vw, 2.5rem);
    font-weight: 700;
    line-height: 1.3;
    margin-bottom: clamp(12px, 1.5vw, 24px);
}

/* BODY TEXT */
body, p {
    font-family: var(--font-body);
    font-size: clamp(0.95rem, 1.2vw, 1.1rem);
    font-weight: 400;
    line-height: 1.6;
    letter-spacing: 0;
}

/* SECTIONS */
section {
    padding: var(--section-padding) var(--section-padding-h);
}

/* BUTTONS */
button, .btn {
    font-family: var(--font-body);
    font-size: 13px;
    font-weight: 600;
    padding: 14px 32px;
    letter-spacing: 0.5px;
}
```

---

## 🚀 Part 10: Implementation Best Practices

### DO's ✅
- ✅ Use CSS variables for all font families
- ✅ Use `clamp()` for responsive font sizes
- ✅ Maintain strict font hierarchy
- ✅ Use consistent spacing scale
- ✅ Test on multiple devices
- ✅ Ensure 16px minimum for body text
- ✅ Use 1.6+ line-height for body text

### DON'Ts ❌
- ❌ Mix font families without purpose
- ❌ Use fixed font sizes (except buttons)
- ❌ Ignore responsive breakpoints
- ❌ Use random padding values
- ❌ Mix letter spacing inconsistently
- ❌ Forget to test on mobile
- ❌ Use font-size below 14px for body

---

## 📊 Part 11: Quick Reference Card

### Font Families
| Use | Font | Weight |
|-----|------|--------|
| h1, h2, h3 | Playfair Display | 700 |
| Body, UI | Inter | 400 |
| Links | Inter | 600 |
| Logo | Great Vibes | 400 |
| Vertical | Oswald | 700 |

### Key Sizes
| Element | Mobile | Desktop |
|---------|--------|---------|
| h1 | 2.5rem | 4.5rem |
| h2 | 2rem | 3.5rem |
| Body | 0.95rem | 1.1rem |
| Label | 0.8rem | 0.95rem |

### Key Padding
| Area | Value |
|------|-------|
| Section | 60-120px (vertical) |
| Card | 20-40px |
| Button | 14px 32px |
| Input | 12px 16px |

---

## 🎨 Part 12: Font Pairing Philosophy

The selected fonts work together beautifully:

1. **Playfair Display** - Elegant, sophisticated serif for headings
2. **Inter** - Clean, modern sans-serif for body and UI
3. **Great Vibes** - Decorative script for accent only

This creates:
- ✅ Professional appearance
- ✅ Good hierarchy
- ✅ Excellent readability
- ✅ Modern aesthetic
- ✅ Brand consistency

---

## ⚠️ Part 13: Common Mistakes to Avoid

| ❌ Mistake | ✅ Correct | Why |
|-----------|-----------|-----|
| Using Great Vibes for body text | Use Inter | Script fonts are hard to read |
| Padding: 17px, 23px, 19px | Use spacing scale: 16px, 24px, 16px | Consistency |
| h1 with Inter font | Use Playfair Display | Playfair is designed for headings |
| Letter-spacing: -0.5px everywhere | Use selective letter-spacing | Context matters |
| Fixed font sizes (16px) | Use clamp() | Not responsive |
| Multiple font families per section | Stick to 2-3 max | Visual chaos |

---

## 📄 Final Notes

- **Last Updated**: April 2, 2026
- **Total Font Families**: 4 (Playfair, Inter, Great Vibes, Oswald)
- **Font Sizes**: 9-level hierarchy
- **Spacing Scale**: 8px base unit
- **Breakpoints**: 3 (Mobile, Tablet, Desktop)

**Implementation Priority**:
1. Set CSS variables (fonts + spacing)
2. Update heading styles
3. Update body text
4. Update component padding
5. Test responsive behavior

---

**End of Document**

**Next Step**: Apply these guidelines across all pages systematically.
