# AUTO GENERATED FILE - DO NOT EDIT

downloadButton <- function(children=NULL, id=NULL, className=NULL, hidden=NULL, target=NULL) {
    
    props <- list(children=children, id=id, className=className, hidden=hidden, target=target)
    if (length(props) > 0) {
        props <- props[!vapply(props, is.null, logical(1))]
    }
    component <- list(
        props = props,
        type = 'DownloadButton',
        namespace = 'download_button',
        propNames = c('children', 'id', 'className', 'hidden', 'target'),
        package = 'downloadButton'
        )

    structure(component, class = c('dash_component', 'list'))
}
