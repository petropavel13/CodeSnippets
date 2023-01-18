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

### SnapKit

#### snpanymake

```swift
<#view#>.snp.makeConstraints {
    <#constraints#>
}
```

#### snpbuttonmake

```swift
<#name#>Button.snp.makeConstraints {
    <#constraints#>
}
```

#### snpimageviewmake

```swift
<#name#>ImageView.snp.makeConstraints {
    <#constraints#>
}
```

#### snplabelmake

```swift
<#name#>Label.snp.makeConstraints {
    <#constraints#>
}
```

#### snpbottomhorizontaltosuper

```swift
$0.bottom.horizontalEdges.equalToSuperview()
```

#### snptophorizontaltosuper

```swift
$0.top.horizontalEdges.equalToSuperview()
```

#### snphorizontaltosuper

```swift
$0.horizontalEdges.equalToSuperview()
```

#### snpverticaltosuper

```swift
$0.verticalEdges.equalToSuperview()
```

#### snpcentertosuper

```swift
$0.center.equalToSuperview()
```

#### snpcenterxtosuper

```swift
$0.centerX.equalToSuperview()
```

#### snpcenterytosuper

```swift
$0.centerY.equalToSuperview()
```

#### snpedgestosuper

```swift
$0.edges.equalToSuperview()
```

#### snpbottomtoview

```swift
$0.bottom.equalTo(<#view#>.snp.<#constraint#>)
```

#### snptoptoview

```swift
$0.top.equalTo(<#view#>.snp.<#constraint#>)
```

#### snphorizontaltoview

```swift
$0.horizontalEdges.equalTo(<#view#>.snp.<#constraint#>)
```

#### snpverticaltoview

```swift
$0.verticalEdges.equalTo(<#view#>.snp.<#constraint#>)
```

#### snpleadingtoview

```swift
$0.leading.equalTo(<#view#>.snp.<#constraint#>)
```

#### snptrailingtoview

```swift
$0.trailing.equalTo(<#view#>.snp.<#constraint#>)
```

#### snpcenterxtoview

```swift
$0.centerX.equalTo(<#view#>.snp.<#constraint#>)
```

#### snpcenterytoview

```swift
$0.centerY.equalTo(<#view#>.snp.<#constraint#>)
```

#### snpedgestoview

```swift
$0.edges.equalTo(<#view#>.snp.<#constraint#>)
```

#### snpsize

```swift
$0.size.equalTo(<#value#>)
```

#### snpheight

```swift
$0.height.equalTo(<#value#>)
```

#### snpwidth

```swift
$0.width.equalTo(<#value#>)
```


### Rx

#### tibehaviorrelay

```swift
private let <#name#>Relay = BehaviorRelay<<#Type#>>(value: <#initialValue#>)
```

#### tipublishrelay

```swift
private let <#name#>Relay = PublishRelay<<#Type#>>()
```

#### tibinder

```swift
var <#name#>Binder: Binder<<#type#>> {
    return Binder(self) { base, value in
        <#code#>
    }
}
```

#### tivardriver

```swift
var <#name#>Driver: Driver<<#type#>> {
    return <#code#>
}
```

#### tidisposebag

```swift
private let disposeBag = DisposeBag()
```

