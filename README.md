# CodeSnippets
Touch Instinct Xcode snippets.

## How to install

### Install all templates
You can clone the complete project in ```~/Library/Developer/Xcode/UserData/```

OR

Clone/Download the project on your machine and paste the .codesnippets file in ```~/Library/Developer/Xcode/UserData/CodeSnippets/```

OR

Clone/Download the project on your machine and run ```./move_snippets.py```. This will clone every snippet into your ```~/Library/Developer/Xcode/UserData/CodeSnippets/``` folder.

### Install partucular templates

#### Install `xcodesnippet`

```sh
./install_xcodesnippet.sh
```

#### Install desired template

```sh
xcodesnippet install Sources/binder.swift
```


## Templates

### Common

#### mark

```swift
// MARK: - <#Title#>
```

### UI

#### tiimageview

```swift
private let <#name#>ImageView = UIImageView()
```

#### tilabel

```swift
private let <#name#>Label = UILabel()
```

#### tibutton

```swift
private let <#name#>Button = UIButton(type: .custom)
```

#### ticontainerview

```swift
private let <#name#>ContainerView = UIView()
```

#### tiaddviews

```swift
override func addViews() {
    super.addViews()

    addSubviews(<#T##views: UIView...##UIView#>)
}
```

#### tibindviews

```swift
override func bindViews() {
    super.bindViews()

    <#views binding#>
}
```

#### ticonfigureappearance

```swift
override func configureAppearance() {
    super.configureAppearance()

    <#views configuration#>
}
```

#### ticonfigurelayout

```swift
override func configureLayout() {
    super.configureLayout()

    <#layout configuration#>
}
```

#### tilocalize

```swift
override func localize() {
    super.localize()

    <#localize views#>
}
```

#### ticonfigurewith

```swift
func configure(with <#ViewModelName#>: <#ViewModelType#>) {
    <#configuration#>
}
```

#### tiappearancemodel

```swift
extension <#View#> {

    public final class Appearance: UIView.BaseAppearance<UIView.<#LayoutType#>>, ViewAppearance {

        public static var defaultAppearance: Self {
            Self()
        }

        public var <#customComponent#>: <#CustomComponentType#>

        public init(layout: UIView.<#LayoutType#> = .defaultLayout,
					backgroundColor: UIColor = .clear,
					roundedCorners: CACornerMask = [],
					cornerRadius: CGFloat = .zero,
					shadow: UIViewShadow? = nil,
					<#customComponent#>: <#CustomComponentType#> = <#defaultValue#>) {

            self.<#customComponent#> = <#customComponent#>

            super.init(layout: layout,
                       backgroundColor: backgroundColor,
                       roundedCorners: roundedCorners,
                       cornerRadius: cornerRadius,
                       shadow: shadow)
        }
    }
}
```

### SnapKit

#### snpanymake

```swift
<#view#>.snp.makeConstraints {
    <#constraints#>
}
```

#### snpimageviewmake

```swift
<#view#>.snp.makeConstraints {
    $0.size.equalTo(<#value#>)
    <#otherConstraints#>
}
```
